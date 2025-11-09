::: wy-grid-for-nav
::: wy-side-scroll
::: wy-side-nav-search
[](../index.html)

::: {role="search"}
:::
:::

::: {.wy-menu .wy-menu-vertical spy="affix" role="navigation" aria-label="Navigation menu"}
-   [What is PlatformIO?](../what-is-platformio.html){.reference
    .internal}

[Getting Started]{.caption-text}

-   [PlatformIO IDE](../integration/ide/pioide.html){.reference
    .internal}
-   [PlatformIO Core (CLI)](../core/index.html){.reference .internal}
-   [PlatformIO Home](../home/index.html){.reference .internal}
-   [PlatformIO Account](../plus/pio-account.html){.reference .internal}
-   [Tutorials and Examples](../tutorials/index.html){.reference
    .internal}

[Configuration]{.caption-text}

-   [platformio.ini](../projectconf/index.html){.reference .internal}
-   [Build
    Configurations](../projectconf/build_configurations.html){.reference
    .internal}
-   [Environment Variables](../envvars.html){.reference .internal}

[Instruments]{.caption-text}

-   [Library Management](../librarymanager/index.html){.reference
    .internal}
-   [Platforms](index.html){.reference .internal}
-   [Frameworks](../frameworks/index.html){.reference .internal}
-   [Boards](../boards/index.html){.reference .internal}
-   [Custom Platform & Board](custom_platform_and_board.html){.reference
    .internal}
    -   [Custom Development Platforms](#){.current .reference .internal}
        -   [Examples](#examples){.reference .internal}
        -   [Packages](#packages){.reference .internal}
        -   [Manifest File [`platform.json`{.docutils .literal
            .notranslate}]{.pre}](#manifest-file-platform-json){.reference
            .internal}
        -   [Build Script [`main.py`{.docutils .literal
            .notranslate}]{.pre}](#build-script-main-py){.reference
            .internal}
        -   [Installation](#installation){.reference .internal}
        -   [Publishing](#publishing){.reference .internal}
    -   [Custom Embedded Boards](creating_board.html){.reference
        .internal}

[Advanced]{.caption-text}

-   [Scripting](../scripting/index.html){.reference .internal}
-   [Debugging](../plus/debugging.html){.reference .internal}
-   [Unit Testing](../advanced/unit-testing/index.html){.reference
    .internal}
-   [Static Code
    Analysis](../advanced/static-code-analysis/index.html){.reference
    .internal}
-   [Remote Development](../plus/pio-remote.html){.reference .internal}

[Integration]{.caption-text}

-   [Cloud & Desktop IDEs](../integration/ide/index.html){.reference
    .internal}
-   [Continuous Integration](../integration/ci/index.html){.reference
    .internal}
-   [Compilation database [`compile_commands.json`{.docutils .literal
    .notranslate}]{.pre}](../integration/compile_commands.html){.reference
    .internal}

[Miscellaneous]{.caption-text}

-   [FAQ](../faq/index.html){.reference .internal}
-   [Release Notes](../core/history.html){.reference .internal}
-   [Migrating from 5.x to 6.0](../core/migration.html){.reference
    .internal}
:::
:::

::: {.section .wy-nav-content-wrap toggle="wy-nav-shift"}
[PlatformIO](../index.html)

::: wy-nav-content

::: rst-content
::: {role="navigation" aria-label="Page navigation"}
-   [](../index.html){.icon .icon-home aria-label="Home"}
-   [Custom Platform & Board](custom_platform_and_board.html)
-   Custom Development Platforms
-   [Edit on
    GitHub](https://github.com/platformio/platformio-docs/blob/develop/platforms/creating_platform.rst){.fa
    .fa-github}

------------------------------------------------------------------------
:::

::: {.document role="main" itemscope="itemscope" itemtype="http://schema.org/Article"}
::: {itemprop="articleBody"}
::: {#custom-development-platforms .section}
[]{#platform-creating}

# [Custom Development Platforms](#id1){.toc-backref role="doc-backlink"}[](#custom-development-platforms "Link to this heading"){.headerlink}

*PlatformIO* can build the same binary code under different host systems
via the single command [[pio run]{.std
.std-ref}](../core/userguide/cmd_run.html#cmd-run){.reference .internal}
without any dependent software or requirements.

A *manifest* describes how to produce binaries for a particular platform
under one or multiple host systems by a set of build scripts,
toolchains, the settings for the most popular embedded boards, etc.

This guide explains how to write manifests, to support building for new
development platforms.

**Step-by-Step Manual**

1.  Choose [[Packages]{.std
    .std-ref}](#platform-creating-packages){.reference .internal} for
    platform

2.  Create [[Manifest File platform.json]{.std
    .std-ref}](#platform-creating-manifest-file){.reference .internal}

3.  Create [[Build Script main.py]{.std
    .std-ref}](#platform-creating-build-script){.reference .internal}

4.  Finish with the [[Installation]{.std
    .std-ref}](#platform-creating-installation){.reference .internal}.

Contents

-   [Custom Development Platforms](#custom-development-platforms){#id1
    .reference .internal}

    -   [Examples](#examples){#id2 .reference .internal}

    -   [Packages](#packages){#id3 .reference .internal}

    -   [Manifest File [`platform.json`{.docutils .literal
        .notranslate}]{.pre}](#manifest-file-platform-json){#id4
        .reference .internal}

    -   [Build Script [`main.py`{.docutils .literal
        .notranslate}]{.pre}](#build-script-main-py){#id5 .reference
        .internal}

    -   [Installation](#installation){#id6 .reference .internal}

    -   [Publishing](#publishing){#id7 .reference .internal}

::: {#examples .section}
## [Examples](#id2){.toc-backref role="doc-backlink"}[](#examples "Link to this heading"){.headerlink}

Please take a look at the source code of existing [PlatformIO
Development
Platforms](https://github.com/topics/platformio-platform){.reference
.external}.
:::

::: {#packages .section}
[]{#platform-creating-packages}

## [Packages](#id3){.toc-backref role="doc-backlink"}[](#packages "Link to this heading"){.headerlink}

Some tools are the same when compiling for several platforms, for
example a common compiler. A *package* is some tool or framework that
can be used when compiling for one or multiple platforms. Even if
multiple platforms use the same package, the package only needs to be
downloaded once. Since each package is pre-built for the different host
systems (Windows, Mac, Linux), developers can get started without first
compiling the tools.

PlatformIO has a registry with pre-built packages for the most popular
operating systems and you can use them in your platform manifest. Custom
packages can be uploaded to the PlatformIO Registry using [[pio pkg
publish]{.std
.std-ref}](../core/userguide/pkg/cmd_publish.html#cmd-pkg-publish){.reference
.internal} command.
:::

::: {#manifest-file-platform-json .section}
[]{#platform-creating-manifest-file}

## [Manifest File [`platform.json`{.docutils .literal .notranslate}]{.pre}](#id4){.toc-backref role="doc-backlink"}[](#manifest-file-platform-json "Link to this heading"){.headerlink}

Each platform definition includes a *manifest file* with a particular
format that is parsed by PlatformIO when handling projects using that
platform.

Here is an example [`platform.json`{.docutils .literal
.notranslate}]{.pre} for the fictitious platform "myplatform":

::: {.highlight-json .notranslate}
::: highlight
    {
      "name": "myplatform",
      "title": "My Platform",
      "description": "My custom development platform",
      "homepage": "https://mycompany.com",
      "license": "Apache-2.0",
      "keywords": ["keyword_1", "keyword_N"],
      "repository": {
        "type": "git",
        "url": "https://github.com/platformio/platform-myplatform.git"
      },
      "version": "0.0.0",
      "frameworks": {
        "%FRAMEWORK_NAME_1%": {
          "package": "framework-%FRAMEWORK_NAME_1%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_1%.py"
        },
        "%FRAMEWORK_NAME_N%": {
          "package": "framework-%FRAMEWORK_NAME_N%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_N%.py"
        }
      },
      "packages": {
        "toolchain-gccarmnoneeabi": {
          "type": "toolchain",
          "owner": "platformio",
          "version": ">=1.40803.0,<1.40805.0"
        },
        "framework-%FRAMEWORK_NAME_1%": {
          "type": "framework",
          "optional": true,
          "version": "~1.10607.0"
        },
        "framework-%FRAMEWORK_NAME_N%": {
          "type": "framework",
          "optional": true,
          "version": "~1.117.0"
        },
        "tool-direct-vcs-url": {
          "type": "uploader",
          "optional": true,
          "version": "https://github.com/user/repo.git"
        }
      }
    }
:::
:::
:::

::: {#build-script-main-py .section}
[]{#platform-creating-build-script}

## [Build Script [`main.py`{.docutils .literal .notranslate}]{.pre}](#id5){.toc-backref role="doc-backlink"}[](#build-script-main-py "Link to this heading"){.headerlink}

Each platform definition must include a [`main.py`{.docutils .literal
.notranslate}]{.pre}.

PlatformIO's build script is based on a next-generation build tool named
[SCons](http://www.scons.org){.reference .external}. PlatformIO has its
own built-in firmware builder [`env.BuildProgram`{.docutils .literal
.notranslate}]{.pre} with deep library search. Please see the following
template as start for developing your own [`main.py`{.docutils .literal
.notranslate}]{.pre}.

::: {.highlight-python .notranslate}
::: highlight
    """
        Build script for test.py
        test-builder.py
    """

    from os.path import join
    from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment

    env = DefaultEnvironment()

    # A full list with the available variables
    # http://www.scons.org/doc/production/HTML/scons-user.html#app-variables
    env.Replace(
        AR="ar",
        AS="gcc",
        CC="gcc",
        CXX="g++",
        OBJCOPY="objcopy",
        RANLIB="ranlib",

        UPLOADER=join("$PIOPACKAGES_DIR", "tool-bar", "uploader"),
        UPLOADCMD="$UPLOADER $SOURCES"
    )

    env.Append(
        ARFLAGS=["..."],

        ASFLAGS=["flag1", "flag2", "flagN"],
        CCFLAGS=["flag1", "flag2", "flagN"],
        CXXFLAGS=["flag1", "flag2", "flagN"],
        LINKFLAGS=["flag1", "flag2", "flagN"],

        CPPDEFINES=["DEFINE_1", "DEFINE=2", "DEFINE_N"],

        LIBS=["additional", "libs", "here"],

        BUILDERS=dict(
            ElfToBin=Builder(
                action=" ".join([
                    "$OBJCOPY",
                    "-O",
                    "binary",
                    "$SOURCES",
                    "$TARGET"]),
                suffix=".bin"
            )
        )
    )

    # The source code of "platformio-build-tool" is here
    # https://github.com/platformio/platformio-core/blob/develop/platformio/builder/tools/platformio.py

    #
    # Target: Build executable and linkable firmware
    #
    target_elf = env.BuildProgram()

    #
    # Target: Build the .bin file
    #
    target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)

    #
    # Target: Upload firmware
    #
    upload = env.Alias(["upload"], target_bin, "$UPLOADCMD")
    AlwaysBuild(upload)

    #
    # Target: Define targets
    #
    Default(target_bin)
:::
:::
:::

::: {#installation .section}
[]{#platform-creating-installation}

## [Installation](#id6){.toc-backref role="doc-backlink"}[](#installation "Link to this heading"){.headerlink}

Using the "myplatform" platform example above:

1.  Create a [`platforms`{.docutils .literal .notranslate}]{.pre}
    directory in [[core_dir]{.std
    .std-ref}](../projectconf/sections/platformio/options/directory/core_dir.html#projectconf-pio-core-dir){.reference
    .internal} if it doesn't exist.

2.  Create a [`myplatform`{.docutils .literal .notranslate}]{.pre}
    directory in [`platforms`{.docutils .literal .notranslate}]{.pre}

3.  Copy the [`platform.json`{.docutils .literal .notranslate}]{.pre}
    and [`builder/main.py`{.docutils .literal .notranslate}]{.pre} files
    to the [`myplatform`{.docutils .literal .notranslate}]{.pre}
    directory.

4.  Search the available platforms via the [[pio platform search]{.std
    .std-ref}](../core/userguide/platforms/cmd_search.html#cmd-platform-search){.reference
    .internal} command. You should see the new [`myplatform`{.docutils
    .literal .notranslate}]{.pre} platform.

5.  Install the [`myplatform`{.docutils .literal .notranslate}]{.pre}
    platform via the [[pio platform install]{.std
    .std-ref}](../core/userguide/platforms/cmd_install.html#cmd-platform-install){.reference
    .internal} command.

Now, you can use [`myplatform`{.docutils .literal .notranslate}]{.pre}
as value for the [[platform]{.std
.std-ref}](../projectconf/sections/env/options/platform/platform.html#projectconf-env-platform){.reference
.internal} option in [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}.
:::

::: {#publishing .section}
## [Publishing](#id7){.toc-backref role="doc-backlink"}[](#publishing "Link to this heading"){.headerlink}

You can publish a development platform to the **PlatformIO Trusted
Registry** using [[pio pkg publish]{.std
.std-ref}](../core/userguide/pkg/cmd_publish.html#cmd-pkg-publish){.reference
.internal} command. Other developers will be able to install it. Every
time when you modify a source code of a development platform you will
need to increment the "version" field in "platform.json" manifest and
re-publish again.

If the published development platform has an issue and you would like to
remove it from the PlatformIO Trusted Registry, please use [[pio pkg
unpublish]{.std
.std-ref}](../core/userguide/pkg/cmd_unpublish.html#cmd-pkg-unpublish){.reference
.internal} command.
:::
:::
:::
:::

::: {.rst-footer-buttons role="navigation" aria-label="Footer"}
[[]{.fa .fa-arrow-circle-left aria-hidden="true"}
Previous](custom_platform_and_board.html "Custom Platform & Board"){.btn
.btn-neutral .float-left accesskey="p" rel="prev"} [Next []{.fa
.fa-arrow-circle-right
aria-hidden="true"}](creating_board.html "Custom Embedded Boards"){.btn
.btn-neutral .float-right accesskey="n" rel="next"}
:::

------------------------------------------------------------------------

::: {role="contentinfo"}
© Copyright 2014-present, PlatformIO.
:::
:::
:::
:::
:::

::: {.rst-versions toggle="rst-versions" role="note" aria-label="Versions"}
[ [ Documentation]{.fa .fa-book} v6.1.19a2 (latest) []{.fa
.fa-caret-down} ]{.rst-current-version toggle="rst-current-version"}

::: rst-other-versions

Versions
:   [latest](/en/)
:   [stable](/en/stable/)

```{=html}
<!-- -->
```

On Github
:   [View](https://github.com/platformio/platformio-docs/blob/develop/platforms/creating_platform.rst)
:   [Edit](https://github.com/platformio/platformio-docs/edit/develop/platforms/creating_platform.rst)

```{=html}
<!-- -->
```

Search

:   ::: {role="search"}
    :::
:::
:::
