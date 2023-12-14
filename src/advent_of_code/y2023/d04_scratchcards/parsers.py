# pyright: reportMissingTypeStubs = false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

from parsy import Parser, regex, string, whitespace

p_optional_whitespace: Parser = regex(r"\s*")
p_number: Parser = regex(r"\d+").map(int) << p_optional_whitespace


def symbol(text: str) -> Parser:
    return string(text) << whitespace
