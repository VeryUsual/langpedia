import os

article_name = input("Please specify your article's name, e.g. Zig, Rust, etc (spaces not allowed): ")

if os.path.exists("content/" + article_name.lower() + ".lp.xml"):
    print("File already exists.")
    exit(0)

template = """
<LPML>
    <TITLE>{{ARTICLE_NAME}}</TITLE>
    <TOC>
        {{ARTICLE_NAME}}\\br\\
        History\\br\\
        Example Code\\br\\
        References\\br\\
    </TOC>
    <RB>
        <H1>{{ARTICLE_NAME}}</H1>
        <IMG>!Language logo here!</IMG>
        <P>Website:</P>
        <LINK where=""></LINK>
    </RB>
    <H1 name="{{ARTICLE_NAME_LOWERCASE}}">{{ARTICLE_NAME}}</H1>
    <P></P>
    <H2 name="history">History</H2>
    <P></P>
    <H2 name="example_code">Example Code</H2>
    <CODE></CODE>
    <H2 name="references">References</H2>
    <CITE></CITE>
</LPML>
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