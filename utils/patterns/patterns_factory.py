#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""patterns_factory -- DESCRIPTION

"""
import os as _os
import sys as _sys

import re


class PatternFactory(object):
    """PatternFactory

    PatternFactory is a object.
    Responsibility: re.compile から_sre.SRE_Pattern 生成

    re.compile 事態が パターンの cache をしているので
    着本的にここでキャッシュ化する必要はない。
    """

    #
    # Flags
    # https://docs.python.org/3/library/re.html#module-contents
    #

    DEBUG = re.DEBUG

    # 指定されると、 ^ が「文字列全体の先頭」と「各行の行頭」を、
    # $ が「文字列全体の末尾」と「各行の末尾」を意味するようになる。
    # 指定されなかった場合のデフォルトのふるまいは、 ^ は「文字列全体の先頭」、
    # $ は「文字列全体の末尾」を意味する。
    MULTILINE = re.MULTILINE
    M = re.M

    # 指定されると、 . が改行を含むあらゆる文字を意味するようになる。
    # 指定されなかった場合のデフォルトのふるまいでは、 . は「改行以外のあらゆる文字」を意味する。
    DOTALL = re.DOTALL
    S = re.S

    IGNORECASE = re.IGNORECASE
    I = re.I

    LOCALE = re.LOCALE
    L = re.L

    TEMPLATE = re.TEMPLATE
    T = re.T

    UNICODE = re.UNICODE
    U = re.U

    VERBOSE = re.VERBOSE
    X = re.X

    @staticmethod
    def make_fullmatch(pattern, flags=0):
        """完全一致正規表現パターンを作成

        make_fullmatch(pattern, flags=0)

        @Arguments:
        - `pattern`:
        - `flags`:

        @Return:

        @Error:
        """
        # require
        if isinstance(pattern, (basestring, )) is False:
            raise TypeError(
                'Must be type basestring. got ({}) type'.format(type(pattern)))

        _flags = int(flags)

        # do

        # ensure
        return re.compile(r"(?:" + pattern + r")\Z", flags=_flags)

    # Regular expression to match all IANA top-level domains.
    # List accurate as of 2010/02/05.  List taken from:
    # http://data.iana.org/TLD/tlds-alpha-by-domain.txt
    # This pattern is auto-generated by frameworks/base/common/tools/make-iana-tld-pattern.py
    TOP_LEVEL_DOMAIN_STR = (
        "((aero|arpa|asia|a[cdefgilmnoqrstuwxz])"
        + "|(biz|b[abdefghijmnorstvwyz])"
        + "|(cat|com|coop|c[acdfghiklmnoruvxyz])"
        + "|d[ejkmoz]"
        + "|(edu|e[cegrstu])"
        + "|f[ijkmor]"
        + "|(gov|g[abdefghilmnpqrstuwy])"
        + "|h[kmnrtu]"
        + "|(info|int|i[delmnoqrst])"
        + "|(jobs|j[emop])"
        + "|k[eghimnprwyz]"
        + "|l[abcikrstuvy]"
        + "|(mil|mobi|museum|m[acdeghklmnopqrstuvwxyz])"
        + "|(name|net|n[acefgilopruz])"
        + "|(org|om)"
        + "|(pro|p[aefghklmnrstwy])"
        + "|qa"
        + "|r[eosuw]"
        + "|s[abcdeghijklmnortuvyz]"
        + "|(tel|travel|t[cdfghjklmnoprtvwz])"
        + "|u[agksyz]"
        + "|v[aceginu]"
        + "|w[fs]"
        + "|(xn\\-\\-0zwm56d|xn\\-\\-11b5bs3a9aj6g|xn\\-\\-80akhbyknj4f|xn\\-\\-9t4b11yi5a|xn\\-\\-deba0ad|xn\\-\\-g6w251d|xn\\-\\-hgbk6aj7f53bba|xn\\-\\-hlcj6aya9esc7a|xn\\-\\-jxalpdlp|xn\\-\\-kgbechtv|xn\\-\\-zckzah)"
        + "|y[etu]"
        + "|z[amw])"
    )

    @staticmethod
    def create_top_level_domain(flags=0, fullmatch=False):
        """トップレベルドメイン

        create_top_level_domain(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.TOP_LEVEL_DOMAIN_STR

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)
        # ensure
        return re.compile(_pattern, flags=_flags)

    YUUBIN_BANGOU_STR = r"[0-9]{3}-[0-9]{4}"

    @staticmethod
    def create_yuubin_bangou(flags=0, fullmatch=False):
        """郵便番号 正規表現パターンを取得

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        create_yuubin_bangou()

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.YUUBIN_BANGOU_STR

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    YUUBIN_BANGOU_NONE_HYPHEN_STR = "[0-9]{7}"

    @staticmethod
    def create_yuubin_bangou_none_hyphen(flags=0, fullmatch=False):
        """郵便番号 正規表現パターンを取得

        create_yuubin_bangou_none_hyphen_regexp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.YUUBIN_BANGOU_NONE_HYPHEN_STR

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    PHONE_NUMBER_JP = (r"(0([1-9]{1}-?[1-9]\d{3}|[1-9]{2}"
                       + r"-\d{3}|[1-9]{2}\d{1}-\d{2}|[1-9]{2}\d{2}-\d{1})"
                       + r"-\d{4}|0[789]0-?\d{4}-\d{4}|050-?\d{4}-\d{4})")

    @staticmethod
    def create_phone_number_jp(flags=0, fullmatch=False):
        """電話番号 正規表現

        例: 077-574-8202, 090-5744-8202, 050-5744-8202
        ×: 0120-574-8202

        create_phone_number_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.PHONE_NUMBER_JP

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    PHONE_NUMBER_NONE_HYPHEN_JP = (
        r"(0([1-9]{1}[1-9]\d{3}|[1-9]{2}"
        + r"\d{3}|[1-9]{2}\d{1}\d{2}|[1-9]{2}\d{2}\d{1})"
        + r"\d{4}|0[789]0\d{4}\d{4}|050\d{4}\d{4})")

    def create_phone_number_none_hyphen_jp(self, flags=0, fullmatch=False):
        """電話番号ハイフン無し 正規表現

        create_phone_number_none_hyphen_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.PHONE_NUMBER_NONE_HYPHEN_JP

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    FIXED_PHONE_NUMBER_JP = (r"0([1-9]{1}-[1-9]\d{3}|[1-9]{2}-\d{3}|[1-9]{2}\d{1}"
                       + r"-\d{2}|[1-9]{2}\d{2}-\d{1})-\d{4}")

    @staticmethod
    def create_fixed_phone_number_jp(flags=0, fullmatch=False):
        """電話番号（固定)

        create_fixed_phone_number_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.FIXED_PHONE_NUMBER_JP

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    FIXED_PHONE_NUMBER_NONE_HYPHEN_JP = (r"0([1-9]{1}[1-9]\d{3}|"
                                         + r"[1-9]{2}\d{3}|[1-9]{2}\d{1}\d{2}|"
                                         + r"[1-9]{2}\d{2}\d{1})\d{4}")

    @staticmethod
    def create_fixed_phone_number_none_hyphen_jp(flags=0, fullmatch=False):
        """SUMMARY

        create_fixed_phone_number_none_hyphen_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.FIXED_PHONE_NUMBER_NONE_HYPHEN_JP

        # do
        if fullmatch is True:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    IP_PHONE_NUMBER_JP_STR = r"050-?\d{4}-?\d{4}"

    @staticmethod
    def create_ip_phone_nuber(flags=0, fullmatch=False):
        """IP電話

        create_ip_phone_nuber(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.IP_PHONE_NUMBER_JP_STR

        # do
        raise NotImplementedError()

        # ensure

        return


    MOBILE_PHONE_NUMBER_JP_STR = r"0[7-9]0-?\d{4}-?\d{4}"

    @staticmethod
    def create_mobile_phone_number_jp(flags=0, fullmatch=False):
        """携帯電話番号 正規表現パターンを取得

        090-0000-0000, 080-0000-0000, 070-0000-0000, 09011112222 パターンに一致


        create_mobile_phone_number_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.MOBILE_PHONE_NUMBER_JP_STR

        # do
        if fullmatch is False:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    IP_ADDRESS_STR = (
        "((25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9])\\.(25[0-5]|2[0-4]"
        + "[0-9]|[0-1][0-9]{2}|[1-9][0-9]|[1-9]|0)\\.(25[0-5]|2[0-4][0-9]|[0-1]"
        + "[0-9]{2}|[1-9][0-9]|[1-9]|0)\\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}"
        + "|[1-9][0-9]|[0-9]))"
    )

    @staticmethod
    def create_ip_address(flags=0, fullmatch=False):
        """SUMMARY

        create_ip_address(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.IP_ADDRESS_STR

        # do
        if fullmatch is False:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    EMAIL_ADDRESS_STR = (
        r"[a-zA-Z0-9\\+\\.\\_\\%\\-\\+]{1,256}"
        + r"\\@"
        + r"[a-zA-Z0-9][a-zA-Z0-9\\-]{0,64}"
        + r"("
        + r"\\."
        + r"[a-zA-Z0-9][a-zA-Z0-9\\-]{0,25}"
        + r")+"
    )

    @staticmethod
    def create_email_address(flags=0, fullmatch=False):
        """SUMMARY

        create_email_address(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.EMAIL_ADDRESS_STR

        # do
        if fullmatch is False:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    DATE_YYYY_MM_DD_STR = r"[12]\d{3}/(0?[1-9]|1[0-2])/([12][0-9]|3[01]|0?[1-9])"

    @staticmethod
    def create_yyyy_mm_dd(flags=0, fullmatch=False):
        """SUMMARY

        create_yyyy_mm_dd(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.DATE_YYYY_MM_DD_STR

        # do
        if fullmatch is False:
            return PatternFactory.make_fullmatch(_pattern, flags=_flags)

        # ensure
        return re.compile(_pattern, flags=_flags)

    DATE_YYYYMMDD_STR = r""

    @staticmethod
    def create_yyyymmdd(flags=0, fullmatch=False):
        """SUMMARY

        create_yyyymmdd(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    FURIGANA_STR = r""

    @staticmethod
    def create_furigana(flags=0, fullmatch=False):
        """フリガナ

        create_furigana(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.FURIGANA_STR

        # do
        raise NotImplementedError()

        # ensure

        return

    GINKOU_CODE_STR = r""

    @staticmethod
    def create_ginkou_code(flags=0, fullmatch=False):
        """銀行コード

        create_ginkou_code(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.GINKOU_CODE_STR

        # do
        raise NotImplementedError()
        # ensure
        return

    SHITEN_CODE_STR = r""

    @staticmethod
    def create_shiten_code(cls, flags=0, fullmatch=False):
        """支店コード

        create_shiten_code(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.SHITEN_CODE_STR

        # do
        raise NotImplementedError()

        # ensure

        return


    KINRI_STR = r""

    @staticmethod
    def create_kinri(flags=0, fullmatch=False):
        """金利

        create_kinri(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    NEN_STR = r""

    @staticmethod
    def create_nen(flags=0, fullmatch=False):
        """年

        create_nen(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require
        _flags = int(flags)
        _pattern = PatternFactory.NEN_STR

        # do

        # ensure

        return

    NENDO_STR = r""

    @staticmethod
    def create_nendo(flags=0, fullmatch=False):
        """年度

        create_nendo(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    NEN_GETSU_HI_STR = r""

    @staticmethod
    def create_nen_getsu_hi(flags=0, fullmatch=False):
        """年月日

        create_nen_getsu_hi(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    SEIBETSU_JP_STR = r""

    @staticmethod
    def create_seibetsu_jp(flags=0, fullmatch=False):
        """性別

        create_seibetsu_jp(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    MENSEKI_STR = r""

    @staticmethod
    def create_menseki(flags=0, fullmatch=False):
        """面積

        create_menseki(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    SHOUHIZEI_STR = r""

    @staticmethod
    def create_shouhizei(flags=0, fullmatch=False):
        """消費税

        create_shouhizei(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    # パスワード

    # クレジットカード番号

    HANKAKU_EISUUJI_STR = r""

    @staticmethod
    def create_hankaku_eisuuji(flags=0, fullmatch=False):
        """半角英数字

        create_hankaku_eisuuji(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    KATAKANA_STR = r""

    @staticmethod
    def create_katakana(flags=0, fullmatch=False):
        """SUMMARY

        create_katakana(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    HANKAKU_STR = r""

    @staticmethod
    def create_hankaku(flags=0, fullmatch=False):
        """半角

        create_hankaku(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    HANKAKU_KATAKANA_STR = r"[ｱ-ﾝﾞﾟｧ-ｫｬ-ｮｰ｡｢｣､]+"

    @staticmethod
    def create_hankaku_katakana(flags=0, fullmatch=False):
        """半角カタカナ

        create_hankaku_katakana(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    ZENKAKU_KATAKANA_STR = r"[ア-ン゛゜ァ-ォャ-ョー「」、]+"

    @staticmethod
    def create_zenkaku_katakana(flags=0, fullmatch=False):
        """SUMMARY

        create_zenkaku_katakana(flags=0, fullmatch=False)

        @Arguments:
        - `flags`:
        - `fullmatch`:

        @Return:

        @Error:
        """
        # require

        # do
        raise NotImplementedError()

        # ensure

        return

    # IPv4

    # IPv6

    # ファイルパス

    # ネットワークパス

    # 半角数値のみ

    # 半角数値のみ

    # 半角英字のみ

    # 半角英字のみ

    # 半角英数字のみ

    # 半角英数記号のみ

    # 8文字以上の半角英数字

    # 6文字以上8文字以内の半角英数字

    # 8文字以下の半角数値

    # 8文字の半角数値

    # 正の小数

    # 正・負の小数

    # 全角ひらがな
    ZENKAKU_HIRAGANA_STR = r"[あ-ん゛゜ぁ-ぉゃ-ょー「」、]+"

    # 全角カタカナ

    # 半角カタカナ

    # 全角文字のみ
    ZENKAKU_STR = r"[ぁ-んァ-ヶー一-龠]+"

    # 特定の拡張子のファイル



def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# patterns_factory.py ends here
