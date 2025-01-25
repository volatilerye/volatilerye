import markdown
import os
import re
import requests

DEFAULT_GITHUB_ICONS = {
    "note": '<svg class="octicon octicon-info mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>',
    "tip": '<svg class="octicon octicon-light-bulb mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 1.5c-2.363 0-4 1.69-4 3.75 0 .984.424 1.625.984 2.304l.214.253c.223.264.47.556.673.848.284.411.537.896.621 1.49a.75.75 0 0 1-1.484.211c-.04-.282-.163-.547-.37-.847a8.456 8.456 0 0 0-.542-.68c-.084-.1-.173-.205-.268-.32C3.201 7.75 2.5 6.766 2.5 5.25 2.5 2.31 4.863 0 8 0s5.5 2.31 5.5 5.25c0 1.516-.701 2.5-1.328 3.259-.095.115-.184.22-.268.319-.207.245-.383.453-.541.681-.208.3-.33.565-.37.847a.751.751 0 0 1-1.485-.212c.084-.593.337-1.078.621-1.489.203-.292.45-.584.673-.848.075-.088.147-.173.213-.253.561-.679.985-1.32.985-2.304 0-2.06-1.637-3.75-4-3.75ZM5.75 12h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM6 15.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg>',
    "important": '<svg class="octicon octicon-report mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v9.5A1.75 1.75 0 0 1 14.25 13H8.06l-2.573 2.573A1.458 1.458 0 0 1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25Zm7 2.25v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 9a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>',
    "warning": '<svg class="octicon octicon-alert mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>',
    "caution": '<svg class="octicon octicon-stop mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>',
}

# デフォルトの設定
default_markers = ["TIP", "NOTE", "IMPORTANT", "WARNING", "CAUTION"]
default_titles = {}
class_prefix = "markdown-alert"


def capitalize(string: str) -> str:
    """最初の文字を大文字化する関数"""
    return string[0].upper() + string[1:]


def parse_markdown_to_alert(md: str) -> str:
    """
    MarkdownをGitHub風のアラートボックスHTMLに変換する。

    :param md: 入力Markdown文字列
    :return: HTML文字列
    """
    # 正規表現の準備
    marker_name_re = "|".join(default_markers)
    pattern = re.compile(
        rf"<blockquote>\s*<p>\[!({marker_name_re})(\s(.+))?\]([^\n\r]*)[\r\n]+((?:(?!</blockquote>).)*?)</p>\s*</blockquote>",
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )

    def replace(text: str) -> str:
        sub_pattern = re.compile(
            rf"<blockquote>\s*<p>\[!({marker_name_re})(\s(.+))?\]([^\n\r]*)[\r\n]+((?:(?!</blockquote>).)*?)</p>\s*</blockquote>",
            re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        match = sub_pattern.match(text.group(0))
        marker = match.group(1).lower()  # マーカー名（小文字化）
        emoji = match.group(3).lower()  # emoji-icon
        icon = (
            DEFAULT_GITHUB_ICONS.get(marker, "") if emoji == "" else emoji
        )  # アイコン
        content = match.group(4).strip()  # アラートの内容
        title = (
            default_titles.get(marker, capitalize(marker)) if content == "" else content
        )  # タイトル
        text = match.group(5).strip()
        return "\n".join(
            [
                f'<div class="{class_prefix} {class_prefix}-{marker}">'
                f'<p class="{class_prefix}-title">{icon}{title}</p>'
                f"<p>{text}</p>"
                f"</div>"
            ]
        )

    return re.sub(pattern, replace, md)


def convert_markdown_to_html(markdown_text):
    with open('converter/.env', 'r') as f:
        TOKEN = re.search('TOKEN="(.+)"', f.read()).group(1)
    
    url = "https://api.github.com/markdown"
    headers = {
        "Content-Type": "application/json",
        "Authorization": TOKEN,
    }
    data = {"text": markdown_text, "mode": "markdown"}
    response = requests.post(url, json=data, headers=headers)

    print(response.text)
    # change string "....md" -> "....html"
    return re.sub(r'<a href="(.+?)\.md">', r'<a href="\1.html">', response.text)


def generate_html_file(md_path: str):
    with open(md_path, "r") as f:
        markdown_text = f.read()
        temp_markdown_text = re.sub(
            "```(.+?)```", "", markdown_text, flags=re.MULTILINE | re.DOTALL
        )
        md = markdown.Markdown(extensions=["toc"])
        md.convert(temp_markdown_text)
        toc = md.toc
        toc = re.sub("#", "#user-content-", toc)
        main_text = convert_markdown_to_html(markdown_text)
        main_text = parse_markdown_to_alert(main_text)

    with open("converter/template.html", "r") as f:
        template_html = f.read()

    html_path = re.sub(
        "^markdown", ".", os.path.splitext(md_path)[0] + ".html"
    )
    if not os.path.exists(html_path):
        os.makedirs(os.path.dirname(html_path), exist_ok=True)

    with open(html_path, "w") as f:
        html_text = re.sub("{toc}", toc, template_html)
        html_text = re.sub("{main}", main_text, html_text)
        html_text = re.sub(
            "{title}",
            md.toc_tokens[0]["name"] if len(md.toc_tokens) > 0 else "untitled",
            html_text,
        )
        html_text = re.sub("{directory}", "../" * (md_path.count("/") - 1), html_text)
        html_text = re.sub("{filepath}", md_path, html_text)
        md_dir_list = md_path.split("/")
        if len(md_dir_list) > 3:
            
            html_text = re.sub(
                "{back_text}", f'<a href="../{md_dir_list[len(md_dir_list)-2]}.html">☜ back</a>', html_text
            )
        elif len(md_dir_list) == 3:
            html_text = re.sub(
                "{back_text}", '<a href="../index.html">☜ back</a>', html_text
            )
        else:
            html_text = re.sub("{back_text}", "[top]", html_text)

        dir_depth = len(md_dir_list) - 2
        contents_info = ""
        for i in range(1, dir_depth+2):
            if len(md_path.split("/")) == 2:
                contents_info = f'index'
                break
            if i == len(md_path.split("/")) - 1:
                contents_info += (
                    md.toc_tokens[0]["name"] if len(md.toc_tokens) > 0 else "untitled"
                )
            elif i == 1:
                contents_info = f'<a href={"../" * dir_depth}index.html>index</a> / '
            else:
                contents_path = "/".join(md_dir_list[:i+1]) +".md"
                with open(contents_path, "r") as g:
                    md_cont = markdown.Markdown(extensions=["toc"])
                    md_cont.convert(g.read())
                    info = (
                        md_cont.toc_tokens[0]["name"]
                        if len(md_cont.toc_tokens) > 0
                        else "untitled"
                    )
                    contents_info += f'<a href="{"../" * (dir_depth - i + 1)}{md_dir_list[len(md_dir_list)-2]}.html">{info}</a> / '

        html_text = re.sub("{contents_info}", contents_info, html_text[:-2])

        f.write(html_text)
