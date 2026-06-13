article_name = input("Please specify your article's name, e.g. Zig, Rust, etc (spaces not allowed): ")
template = """
<lpml>
    <title>{{ARTICLE_NAME}}</title>
    <tableofcontents>
        {{ARTICLE_NAME}}\\br\\
        History\\br\\
        Example Code\\br\\
        References\\br\\
    </tableofcontents>
    <rightbox>
        <h1>{{ARTICLE_NAME}}</h1>
        <img>!Language logo here!</img>
        <p>Website:</p>
        <link where=""></link>
    </rightbox>
    <h1 name="{{ARTICLE_NAME_LOWERCASE}}">{{ARTICLE_NAME}}</h1>
    <p></p>
    <h2 name="history">History</h2>
    <p></p>
    <h2 name="example_code">Example Code</h2>
    <code></code>
    <h2 name="references">References</h2>
    <cite></cite>
</lpml>
""".strip()

replacements = {
    "{{ARTICLE_NAME}}": article_name,
    "{{ARTICLE_NAME_LOWERCASE}}": article_name.lower(),
}

with open("content/" + article_name.lower() + ".lp.xml", 'w') as f:
    contents = template
    for k, v in replacements.items():
        contents = contents.replace(k, v)
    f.write(contents)

print("Generated content/" + article_name.lower() + ".lp.xml.")