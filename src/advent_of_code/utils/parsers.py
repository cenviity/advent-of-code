# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

from parsy import Parser, regex, string

p_optional_whitespace: Parser = regex(r"\s*")


def lexeme(parser: Parser) -> Parser:
    return parser << p_optional_whitespace


def symbol(text: str) -> Parser:
    return lexeme(string(text))


p_number: Parser = lexeme(regex(r"\d+")).map(int)
p_letters: Parser = lexeme(regex(r"\w+"))
