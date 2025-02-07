document.addEventListener("DOMContentLoaded", function () {
  // --- 数式のレンダリング ---
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
    ],
    ignoredTags: [
      "script",
      "noscript",
      "style",
      "textarea",
      "pre",
      "code"
    ],
    preProcess: function (text) {
      // \$ を通貨記号として扱うためにエスケープされたものを置換
      return text.replace(/\\\$/g, "ESCAPED_DOLLAR");
    },
  });

  // 一時的に置換したテキストを元に戻す
  document.body.innerHTML = document.body.innerHTML.replace(/ESCAPED_DOLLAR/g, "$");

  // --- 目次自動生成 ---
  // メインコンテンツ内の h1～h6 を対象に目次を生成する
  const content = document.querySelector('.contents');
  if (!content) return;

  const headers = content.querySelectorAll('h1, h2, h3, h4, h5, h6');
  if (headers.length === 0) return;

  // 目次コンテナのプレースホルダー :toc: を削除
  const tocContainer = document.querySelector('.toc');
  tocContainer.innerHTML = tocContainer.innerHTML.replace(':toc:', '');

  // トップレベルの UL を生成
  const tocRoot = document.createElement('ul');
  tocContainer.appendChild(tocRoot);

  // 初期スタックを「レベル1」として設定（h1がトップレベルになる）
  const listStack = [{
    level: 1,
    element: tocRoot
  }];

  headers.forEach((header, index) => {
    // 見出しにIDがなければ自動付与（アンカーリンク用）
    if (!header.id) {
      header.id = 'header-' + index;
    }
    const headerLevel = parseInt(header.tagName.substring(1));

    // 現在のスタックの最上位を取得
    let current = listStack[listStack.length - 1];

    if (headerLevel > current.level) {
      // ヘッダーのレベルが深い場合は、子リストを作成する
      // 現在のリスト項目の最後の <li> に新たな <ul> を追加
      let lastLi = current.element.lastElementChild;
      if (!lastLi) {
        // もしリスト項目が無ければ、新たに作成
        lastLi = document.createElement('li');
        current.element.appendChild(lastLi);
      }
      const newList = document.createElement('ul');
      lastLi.appendChild(newList);
      current = { level: headerLevel, element: newList };
      listStack.push(current);
    } else if (headerLevel < current.level) {
      // ヘッダーのレベルが浅い場合は、適切なレベルまでスタックから戻す
      while (listStack.length && headerLevel < listStack[listStack.length - 1].level) {
        listStack.pop();
      }
      current = listStack[listStack.length - 1];
    }
    // ヘッダーのレベルが同じ場合は current をそのまま使用

    // リンク付きのリスト項目を作成
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + header.id;
    a.textContent = header.textContent;
    li.appendChild(a);
    current.element.appendChild(li);
  });
});
