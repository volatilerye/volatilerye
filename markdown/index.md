# volatile rye.

![restio](restio.png)


## 07734 / hELLO

ここは volatile rye （ボラティル ライ） が数学に関することを復習を兼ねてまとめていく為だけのサイトです.

まだ作ったばっかりなのでなんにもないよ．

不定期に更新予定ですので, 忘れた頃にまた見に来てくださいね.

---

## テスト用
デバッグ用.
- [テスト](test/test.md)

---

## contents

(まだ準備中．．．．．．)

### 解析学 (analysis)
- (準備中)

### 統計学 (statistics)
- (準備中)

### 確率論 (probability theory)
- (準備中)

### 幾何学 (geometry)
- [位相幾何学](geometry/topology.md)

### 代数学 (algebra)
- (準備中)

### 集合論 (set theory)
- (準備中)

### 論理学 (logic theory)
- (準備中)


## このサイトについて

次の条件を満たすようなWebサービスが中々見つからなかったため, サイトを自作しました.

- GFM (GitHub Flacored Markdown) 準拠の Markdown 記法に対応
- $\LaTeX$ に対応 （数学中心の記事を多く書くので必須）
- css カスタマイズ可 (なるべく Github に近い見た目にしたかった)
- ファイルのバックアップ・バージョン管理が可能
- 無料かつ広告なしで運営できる (GitHub Pages を利用)

(あと自作したかったというのもある...)

- css は [github-markdown-css](https://github.com/sindresorhus/github-markdown-css) のコードを流用
- Markdown → HTML の変換は Github の [Rest API](https://docs.github.com/en/rest/markdown) に request を送り変換
- $\LaTeX$ を正常にレンダリングできるような converter を実装
- [GitHub Flavored Markdown] に独自実装したアラート記法（定義・定理等のブロック）を追加
- $\LaTeX$ のレンダリングには [$\KaTeX$](https://katex.org/) を利用

