# MecabUnidic

This add-on adds support for the UniDic Japanese dictionary which can be used by other add-ons such as [MorphMan](https://github.com/landonepps/MorphMan21).

## Usage

Support for Windows, Linux and macOS.

**Download the latest release [here](https://github.com/Luukuton/MecabUnidic/releases/tag/v1.0)** and extract it to the Anki's add-on directory (`Anki2\addons21`).

## Compiling release

- `git clone` this repository

- Get files from [support/Windows](support/Windows), [support/Linux](support/Linux) or [support/macOS](support/macOS) and place them to the root of [support](support). Those directories can now be deleted.

- Get `dicrc`, `char.bin`, `matrix.bin`, `model.bin`, `sys.dic` and `unk.dic` from [unidic-csj-x.y.z.zip](https://unidic.ninjal.ac.jp/download) and place them to the same support directory.

- Move the whole cloned directory to Anki's addon directory.

## Notes / Changelog

- [Original repository (ianki/MecabUnidic)](https://github.com/ianki/MecabUnidic)
- Updated old UniDic (ver.2016.3) to the latest at the time of writing: UniDic 3.1.0 (2021-04-01)
- Updated Windows, Linux and macOS binaries of MeCab from 0.98pre3 to 0.996

## Libraries used

- [UniDic 3.1.0 (2021-04-01)](https://unidic.ninjal.ac.jp/download#unidic_csj) for modern spoken language (現代話し言葉).
- [MeCab 0.996 (2013-02-18)](https://taku910.github.io/mecab/)
  - [MeCab Windows](support/Windows) Binaries from the website
  - [MeCab Linux](support/Linux): Built by @Luukuton from the source code on the website
  - [MeCab macOS](support/Linux): Built by @kebifurai from the source code on the website
