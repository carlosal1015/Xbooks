## [1.7.6](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.5...v1.7.6) (2020-03-17)


### Bug Fixes

* **package:** update commander to version 4.0.0 ([b75295e](https://github.com/xsoft-technologies/Xbooks/commit/b75295e))
* **package:** update update-notifier to version 4.0.0 ([4de991a](https://github.com/xsoft-technologies/Xbooks/commit/4de991a))

## [1.7.5](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.4...v1.7.5) (2020-02-14)


### Bug Fixes

* regexp match fixed to only root files ([f39e579](https://github.com/xsoft-technologies/Xbooks/commit/f39e579))

## [1.7.4](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.3...v1.7.4) (2020-02-14)


### Bug Fixes

* skip pdf script ([ca1e713](https://github.com/xsoft-technologies/Xbooks/commit/ca1e713))

## [1.7.3](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.2...v1.7.3) (2019-09-09)


### Bug Fixes

* a ridiculous patch of all the time! ([c838a81](https://github.com/xsoft-technologies/Xbooks/commit/c838a81))

## [1.7.2](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.1...v1.7.2) (2019-09-09)


### Bug Fixes

* publish script pushes after stash has been apllied back ([c5c5c0b](https://github.com/xsoft-technologies/Xbooks/commit/c5c5c0b))

## [1.7.1](https://github.com/xsoft-technologies/Xbooks/compare/v1.7.0...v1.7.1) (2019-09-09)


### Bug Fixes

* CLI patches ([f9c3cd6](https://github.com/xsoft-technologies/Xbooks/commit/f9c3cd6))
* resolves minor placifier errors ([bfdb76b](https://github.com/xsoft-technologies/Xbooks/commit/bfdb76b))
* resolves tex des path correctly ([f5eb1e5](https://github.com/xsoft-technologies/Xbooks/commit/f5eb1e5))
* stashing now includes all files, fixes [#98](https://github.com/xsoft-technologies/Xbooks/issues/98) ([d2868cf](https://github.com/xsoft-technologies/Xbooks/commit/d2868cf))

# [1.7.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.6.1...v1.7.0) (2019-09-08)


### Bug Fixes

* resolves bs4 and string conflicts, fixes [#102](https://github.com/xsoft-technologies/Xbooks/issues/102) ([e31a517](https://github.com/xsoft-technologies/Xbooks/commit/e31a517))
* stash mechanism to avoid sync conflicts, fixes [#98](https://github.com/xsoft-technologies/Xbooks/issues/98) ([24cd50b](https://github.com/xsoft-technologies/Xbooks/commit/24cd50b))
* tex template installation for pdf, and placifier replacment of placeholder gh_namespace instead of gh_username, fixes [#100](https://github.com/xsoft-technologies/Xbooks/issues/100), fixes99 ([cd15660](https://github.com/xsoft-technologies/Xbooks/commit/cd15660))


### Features

* py env specific config template installation, fixes [#103](https://github.com/xsoft-technologies/Xbooks/issues/103), ffixes [#104](https://github.com/xsoft-technologies/Xbooks/issues/104) ([5332067](https://github.com/xsoft-technologies/Xbooks/commit/5332067))

## [1.6.1](https://github.com/xsoft-technologies/Xbooks/compare/v1.6.0...v1.6.1) (2019-09-08)


### Bug Fixes

* fixes [#28](https://github.com/xsoft-technologies/Xbooks/issues/28), new CI scripts, GreyBoy theme refactorization, and publish script PAT var changed ([b32d13f](https://github.com/xsoft-technologies/Xbooks/commit/b32d13f))

# [1.6.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.5.3...v1.6.0) (2019-09-07)


### Bug Fixes

* import errors in new styled code ([9bad1df](https://github.com/xsoft-technologies/Xbooks/commit/9bad1df))


### Features

* bibtex support for pdf files, fixes [#31](https://github.com/xsoft-technologies/Xbooks/issues/31), and deprecates [#91](https://github.com/xsoft-technologies/Xbooks/issues/91) ([eddd42e](https://github.com/xsoft-technologies/Xbooks/commit/eddd42e))

## [1.5.3](https://github.com/xsoft-technologies/Xbooks/compare/v1.5.2...v1.5.3) (2019-09-06)


### Bug Fixes

* changed alert exit code 1 to 0 ([b069726](https://github.com/xsoft-technologies/Xbooks/commit/b069726))
* resolves multicommit transformation flaw ([7d9d1aa](https://github.com/xsoft-technologies/Xbooks/commit/7d9d1aa))

## [1.5.2](https://github.com/xsoft-technologies/Xbooks/compare/v1.5.1...v1.5.2) (2019-09-06)


### Bug Fixes

* resolves logical flow of closing script, fixes [#88](https://github.com/xsoft-technologies/Xbooks/issues/88) ([94e9366](https://github.com/xsoft-technologies/Xbooks/commit/94e9366))

## [1.5.1](https://github.com/xsoft-technologies/Xbooks/compare/v1.5.0...v1.5.1) (2019-09-06)


### Bug Fixes

* syntax errors ([2ff5f36](https://github.com/xsoft-technologies/Xbooks/commit/2ff5f36))

# [1.5.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.4.0...v1.5.0) (2019-09-06)


### Bug Fixes

* authorized post req for closing script, fixes [#86](https://github.com/xsoft-technologies/Xbooks/issues/86) ([7de2e24](https://github.com/xsoft-technologies/Xbooks/commit/7de2e24))
* closing script failures, fixes [#88](https://github.com/xsoft-technologies/Xbooks/issues/88) ([11160d1](https://github.com/xsoft-technologies/Xbooks/commit/11160d1))
* correction in update notifications, fixes [#80](https://github.com/xsoft-technologies/Xbooks/issues/80) ([5d57587](https://github.com/xsoft-technologies/Xbooks/commit/5d57587))
* dependancy markdown2 installation on Xbooks container, fixes [#81](https://github.com/xsoft-technologies/Xbooks/issues/81) ([04c4bbe](https://github.com/xsoft-technologies/Xbooks/commit/04c4bbe))
* introduces logical Close Codes for realistic CI pipeline statuses, fixes [#77](https://github.com/xsoft-technologies/Xbooks/issues/77) ([6c5a262](https://github.com/xsoft-technologies/Xbooks/commit/6c5a262))
* Merge pull request [#89](https://github.com/xsoft-technologies/Xbooks/issues/89) from xsoft-technologies/next ([cd9ea76](https://github.com/xsoft-technologies/Xbooks/commit/cd9ea76)), closes [#88](https://github.com/xsoft-technologies/Xbooks/issues/88)
* pipeline script failure due to unsupported concatenation[skip ci] ([6bcb4fa](https://github.com/xsoft-technologies/Xbooks/commit/6bcb4fa))
* resolved Xbooks docker container dependancies for pip ([f5bcc9f](https://github.com/xsoft-technologies/Xbooks/commit/f5bcc9f))


### Features

* automatically enebles README.md file as homepage if notebooks/welcome.ipynb doesn't exist, fixes [#57](https://github.com/xsoft-technologies/Xbooks/issues/57) ([088285e](https://github.com/xsoft-technologies/Xbooks/commit/088285e))
* automatically enebles README.md file as homepage if notebooks/welcome.ipynb doesn't exist, fixes [#57](https://github.com/xsoft-technologies/Xbooks/issues/57) ([cc1a318](https://github.com/xsoft-technologies/Xbooks/commit/cc1a318))
* introduces 411641ef3f0a3212fcab50f8ccadf1c27980d211 for publish scripts, fixes [#75](https://github.com/xsoft-technologies/Xbooks/issues/75) ([bdb5b9c](https://github.com/xsoft-technologies/Xbooks/commit/bdb5b9c))
* introduces fetching of PAT ENV VAR for publish scripts, fixes [#75](https://github.com/xsoft-technologies/Xbooks/issues/75) ([84e8cbf](https://github.com/xsoft-technologies/Xbooks/commit/84e8cbf))


# [1.4.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.3.3...v1.4.0) (2019-08-30)


### Bug Fixes

* solves logical errors produced by multicommit transformation fixes [#72](https://github.com/xsoft-technologies/Xbooks/issues/72) and fixes [#16](https://github.com/xsoft-technologies/Xbooks/issues/16) ([5e3a4da](https://github.com/xsoft-technologies/Xbooks/commit/5e3a4da))


### Features

* a stable chore mechanism for multicommit transformtion ([ac6294e](https://github.com/xsoft-technologies/Xbooks/commit/ac6294e))
* completely new way of multicommit transformation it gives a way to ([277a43f](https://github.com/xsoft-technologies/Xbooks/commit/277a43f))
* introduces chores mechanism to support multicommit transformation ([f2235ea](https://github.com/xsoft-technologies/Xbooks/commit/f2235ea))

## [1.3.3](https://github.com/xsoft-technologies/Xbooks/compare/v1.3.2...v1.3.3) (2019-08-29)


### Bug Fixes

* [#70](https://github.com/xsoft-technologies/Xbooks/issues/70) hexsha7 as a string and an object are introduced seperately ([11f4361](https://github.com/xsoft-technologies/Xbooks/commit/11f4361))
* [#71](https://github.com/xsoft-technologies/Xbooks/issues/71) better temp workspace cleaning script ([fb08db2](https://github.com/xsoft-technologies/Xbooks/commit/fb08db2))

## [1.3.2](https://github.com/xsoft-technologies/Xbooks/compare/v1.3.1...v1.3.2) (2019-08-29)


### Bug Fixes

* [#68](https://github.com/xsoft-technologies/Xbooks/issues/68) resolved Xbooksrc file fetching error ([05fdd39](https://github.com/xsoft-technologies/Xbooks/commit/05fdd39))

## [1.3.1](https://github.com/xsoft-technologies/Xbooks/compare/v1.3.0...v1.3.1) (2019-08-29)


### Bug Fixes

* importing path of ccc ([a1289a2](https://github.com/xsoft-technologies/Xbooks/commit/a1289a2))

# [1.3.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.2.2...v1.3.0) (2019-08-29)


### Bug Fixes

* [#66](https://github.com/xsoft-technologies/Xbooks/issues/66) just a try! ([2562824](https://github.com/xsoft-technologies/Xbooks/commit/2562824))


### Features

* Xbooks update notifications ([2040183](https://github.com/xsoft-technologies/Xbooks/commit/2040183))

## [1.2.2](https://github.com/xsoft-technologies/Xbooks/compare/v1.2.1...v1.2.2) (2019-08-29)


### Bug Fixes

* [#60](https://github.com/xsoft-technologies/Xbooks/issues/60) fixes problem of fetching untransformed commits ([7c545b9](https://github.com/xsoft-technologies/Xbooks/commit/7c545b9))

## [1.2.1](https://github.com/xsoft-technologies/Xbooks/compare/v1.2.0...v1.2.1) (2019-08-29)


### Bug Fixes

* [#58](https://github.com/xsoft-technologies/Xbooks/issues/58) and [#56](https://github.com/xsoft-technologies/Xbooks/issues/56) allows to run Xbooks on any machines ([536ed20](https://github.com/xsoft-technologies/Xbooks/commit/536ed20))



## [1.2.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.1.0...v1.2.0) (2019-08-28)


### Features

multicommmit analysis, and transformation, patch to [#45](https://github.com/xsoft-technologies/Xbooks/issues/45) 
[(546f0a3)](https://github.com/xsoft-technologies/Xbooks/commit/546f0a3)



## [1.1.0](https://github.com/xsoft-technologies/Xbooks/compare/v1.0.0...v1.1.0) (2019-08-27)

### Features
tabular cards for subdirs, newly created first order; fix [#19](https://github.com/xsoft-technologies/Xbooks/issues/19) [(8c2e67e)](https://github.com/xsoft-technologies/Xbooks/commit/8c2e67e)



## [1.1.0](https://github.com/xsoft-technologies/Xbooks/releases/tag/v1.0.0) (2019-08-08)

### Features
- add new Xtheme; just an temp [(da9249f)](https://github.com/xsoft-technologies/Xbooks/commit/da9249f)
- basic installer and server [(62fb83a)](https://github.com/xsoft-technologies/Xbooks/commit/62fb83a)
- basic Xbooks_cli\r\nonly an 'init' command is developed [(ce605be)](https://github.com/xsoft-technologies/Xbooks/commit/ce605be)
- converter is developed and is ready to use! [(0ade118)](https://github.com/xsoft-technologies/Xbooks/commit/0ade118)


## [0.9.0](https://github.com/xsoft-technologies/Xbooks/releases/tag/0.9.0)
DEPRECATED INITIAL RELEASE
