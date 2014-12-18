# Compiler Principles课程项目

### 支持解析的标签

###### 块级

- 普通段落
- 井号标题
- blockquote
- 有序列表（支持嵌套列表）
- 无序列表（支持嵌套列表）
- 标准块级代码
- 多星号/等号水平分隔符
- 图片

###### 行内

- 着重
- 行内代码
- 有title超链接
- 无title超链接
- 斜体字
- 普通文字


### BNF

```
<Article> ::= <Article> <Block> | ε

<Block> ::= <Paragraph>
            | <HeadingLevel1>
            | <HeadingLevel2>
            | <HeadingLevel3>
            | <HeadingLevel4>
            | <HeadingLevel5>
            | <HeadingLevel6>
            | <BlockQuote>
            | <UnOrderedList>
            | <OrderedList>
            | <Code>
            | <Horizontal>
            | <Image>

<Inline> ::= <Strong>
            | <InlineCode>
            | <TitledLink>
            | <UntitledLink>
            | <Italic>
            | <Plain>

<HeadingLevel1> ::= # <Inline>
<HeadingLevel2> ::= ## <Inline>
<HeadingLevel3> ::= ### <Inline>
<HeadingLevel4> ::= #### <Inline>
<HeadingLevel5> ::= ##### <Inline>
<HeadingLevel6> ::= ###### <Inline>

<BlockQuote>    ::= > <Inline> | > <Inline> \n <BlockQuote>

```