# 剪映 UI 设计系统（从 CSS / JS 资产还原）

- 资产：CSS **123** 个（5.3 MB）/ JS **735** / QML **354** / SVG **645**
- 技术指纹：{"react": 103, "Lynx": 43, "react-flow": 25, "immer": 9, "fabric.js": 2, "lv- 组件库": 2, "vue": 2, "zustand": 1, "konva": 1}

## 一、CSS 自定义属性（它的令牌表，直接可抄）

| 令牌 | 主要取值 |
| --- | --- |
| `--accent` | `var(--skill-accent,#00cae0)` |
| `--accent-hover` | `var(--skill-accent-hover,#00b1cc)` |
| `--accent-soft` | `var(--skill-accent-soft,#202d30)` |
| `--accent-text` | `var(--skill-accent-text,#00cae0)` |
| `--ai-loading-radius` | `12px` |
| `--ai-loading-spark-color-field` | `#fff` |
| `--ai-loading-spark-grid-size` | `20px` / `8.333333cqmin` |
| `--ai-loading-spark-shape` | `url("data:image/svg+xml` |
| `--ai-loading-surface` | `rgba(28,28,28,.95)` / `rgba(38,38,38,.95)` / `#1c1c1c` |
| `--alpha-10b` | `rgba(var(--black-00-rgb),0.1)` |
| `--alpha-20w` | `rgba(var(--white-00-rgb),0.2)` |
| `--alpha-2w` | `rgba(var(--white-00-rgb),0.02)` |
| `--alpha-30b` | `rgba(var(--black-00-rgb),0.3)` |
| `--alpha-3w` | `rgba(var(--white-00-rgb),0.03)` |
| `--alpha-40b` | `rgba(var(--black-00-rgb),0.4)` |
| `--alpha-50w` | `rgba(var(--white-00-rgb),0.5)` |
| `--alpha-60b` | `rgba(var(--black-00-rgb),0.6)` |
| `--alpha-60w` | `rgba(var(--white-00-rgb),0.6)` |
| `--alpha-80w` | `rgba(var(--white-00-rgb),0.8)` |
| `--alpha-8w` | `rgba(var(--white-00-rgb),0.08)` |
| `--alpha-9w` | `rgba(var(--white-00-rgb),0.09)` |
| `--alt-text-add-image` | `url(images/editor-toolbar-edit.svg) !important` / `url(images/altText_add.svg)` |
| `--alt-text-done-color` | `var(
      --color-accent-attention,
      light-dark(#2ac3a` / `var(--editor-toolbar-fg-color)` |
| `--alt-text-done-image` | `url(images/altText_done.svg)` |
| `--alt-text-hover-done-color` | `var(--alt-text-done-color)` / `var(--editor-toolbar-hover-fg-color)` |
| `--alt-text-hover-warning-color` | `var(--alt-text-warning-color)` / `var(--editor-toolbar-hover-fg-color)` |
| `--alt-text-tooltip-bg` | `light-dark(#f0f0f4, #1c1b22)` / `Canvas` |
| `--alt-text-tooltip-border` | `var(--border-color-interactive, #8f8f9d)` / `var(--border-color, CanvasText)` |
| `--alt-text-tooltip-fg` | `var(
              --text-color,
              light-dark(#1` / `var(--text-color, CanvasText)` |
| `--alt-text-tooltip-shadow` | `0 2px 6px 0 light-dark(rgb(58 57 68 / 0.2), #15141a)` / `none` |
| `--alt-text-warning-color` | `light-dark(#0090ed, #80ebff)` / `var(--editor-toolbar-fg-color)` |
| `--annotation-unfocused-field-background` | `url("data:image/svg+xml` |
| `--annotation-unfocused-field-filter` | `url("data:image/svg+xml` |
| `--arcoblue-1` | `232,243,255` / `0,13,77` |
| `--arcoblue-10` | `0,13,77` / `234,244,255` |
| `--arcoblue-2` | `190,218,255` / `4,27,121` |
| `--arcoblue-3` | `148,191,255` / `14,50,166` |
| `--arcoblue-4` | `106,161,255` / `29,77,210` |
| `--arcoblue-5` | `64,128,255` / `48,111,255` / `0,193,205` |
| `--arcoblue-6` | `22,93,255` / `60,126,255` / `0,193,205` |
| `--arcoblue-7` | `14,66,210` / `104,159,255` |
| `--arcoblue-8` | `7,44,166` / `147,190,255` |
| `--arcoblue-9` | `3,26,121` / `190,218,255` |
| `--asset-card-flow-angle` | `290deg` / `360deg` / `500deg` |
| `--asset-card-flow-end` | `0deg` / `85deg` |
| `--asset-card-flow-solid-end` | `0deg` / `63.75deg` |
| `--asset-card-flow-solid-start` | `0deg` / `21.25deg` |
| `--asset-card-outline-offset` | `3px` / `2px` |
| `--asset-card-radius` | `8px` |
| `--attachment-bg-color` | `light-dark(
        rgb(0 0 0 / 0.15),
        rgb(255 255 2` |
| `--attachment-color` | `light-dark(rgb(0 0 0 / 0.8), rgb(255 255 255 / 0.8))` |
| `--attachment-hover-color` | `light-dark(
        rgb(0 0 0 / 0.9),
        rgb(255 255 25` |
| `--bg` | `HighlightText` |
| `--bg-hover` | `var(
    --button-background-color-hover,
    light-dark(#e0` / `var(--bg)` |
| `--black-0` | `#070709` |
| `--black-0-rgb` | `7,7,9` |
| `--black-00` | `#000` |
| `--black-00-rgb` | `0,0,0` |
| `--black-0a` | `rgba(var(--black-0-rgb),0.9)` |
| `--black-1` | `#1b1b1c` |
| `--black-2` | `#202023` |
| `--black-3` | `#252528` |
| `--black-4` | `#29292d` |
| `--black-5` | `#343337` |
| `--blend-mode` | `multiply` / `difference` |
| `--blue-1` | `232,247,255` / `0,26,77` |
| `--blue-10` | `0,26,77` / `234,248,255` |
| `--blue-2` | `195,231,254` / `5,47,120` |
| `--blue-3` | `159,212,253` / `19,76,163` |
| `--blue-4` | `123,192,252` / `41,113,207` |
| `--blue-5` | `87,169,251` / `70,154,250` |
| `--blue-6` | `52,145,250` / `90,170,251` |
| `--blue-7` | `32,108,207` / `125,193,252` |
| `--blue-8` | `17,75,163` / `161,213,253` |
| `--blue-9` | `6,48,120` / `198,232,254` |
| `--border-radius-circle` | `50%` |
| `--border-radius-large` | `8px` |
| `--border-radius-medium` | `4px` |
| `--border-radius-none` | `0` |
| `--border-radius-small` | `2px` |
| `--box-shadow-light-level-1` | `0px 6px 16px #0404040f` |
| `--button-active-bg` | `var(
    --button-background-color-active,
    light-dark(rg` / `var(--button-background-color-active, SelectedItemText)` |
| `--button-active-border-color` | `var(--views-button-border-color)` / `var(--button-border-color-active, ButtonText)` |
| `--button-active-fg` | `var(--views-text-color)` / `var(--button-text-color-active, SelectedItem)` |
| `--button-bg` | `var(
    --button-background-color,
    light-dark(rgb(21 20` / `var(--button-background-color, ButtonFace)` |
| `--button-comment-active-bg` | `light-dark(#cfcfd8, #5b5b66)` / `Highlight` |
| `--button-comment-active-border` | `none` |
| `--button-comment-active-color` | `var(--button-comment-color)` / `HighlightText` |
| `--button-comment-bg` | `transparent` / `ButtonFace` |
| `--button-comment-border` | `none` / `1px solid ButtonText` |
| `--button-comment-color` | `var(--main-color)` / `ButtonText` |
| `--button-comment-hover-bg` | `light-dark(#e0e0e6, #52525e)` / `Highlight` |
| `--button-comment-hover-color` | `var(--button-comment-color)` / `HighlightText` |
| `--button-dimension` | `24px` |
| `--button-disabled-opacity` | `0.4` / `0.6` / `1` |
| `--button-fg` | `var(--views-text-color)` / `var(--button-text-color, ButtonText)` |
| `--button-focus-border-color` | `light-dark(white, black)` / `none` |
| `--button-focus-no-bg` | `color-mix(
    in srgb,
    var(--views-text-color),
    tra` / `var(--button-background-color, ButtonFace)` |
| `--button-focus-outline-color` | `var(
    --focus-outline-color,
    light-dark(#0062fa, #00c` / `var(--focus-outline-color, CanvasText)` |
| `--button-hover-bg` | `var(
    --button-background-color-hover,
    light-dark(rgb` / `var(--button-background-color-hover, SelectedItemText)` |
| `--button-hover-border-color` | `var(--views-button-border-color)` / `var(--button-border-color-hover, SelectedItem)` |
| `--button-hover-fg` | `var(--views-text-color)` / `var(--button-text-color-hover, SelectedItem)` |
| `--button-no-bg` | `var(--button-background-color-toolbar, transparent)` / `var(--button-background-color, ButtonFace)` |
| `--button-primary-active-bg-color` | `var(
    --button-background-color-primary-active,
    light` / `var(
      --button-background-color-primary-active,
      S` |
| `--button-primary-active-border-color` | `var(--button-primary-active-bg-color)` / `var(
      --button-border-color-primary-active,
      Butto` |
| `--button-primary-active-fg-color` | `var(--button-primary-fg-color)` / `var(
      --button-text-color-primary-active,
      Highlig` |
| `--button-primary-bg-color` | `var(
    --button-background-color-primary,
    light-dark(#` / `var(
      --button-background-color-primary,
      ButtonTe` |
| `--button-primary-border-color` | `var(--button-primary-bg-color)` / `var(
      --button-border-color-primary,
      ButtonText
 ` |
| `--button-primary-disabled-bg-color` | `var(--button-primary-bg-color)` / `var(
      --button-background-color-primary-disabled,
     ` |
| `--button-primary-disabled-border-color` | `var(--button-primary-border-color)` / `var(
      --button-border-color-primary-disabled,
      Gra` |
| `--button-primary-disabled-fg-color` | `var(--button-primary-fg-color)` / `var(
      --button-text-color-primary-disabled,
      Butto` |
| `--button-primary-fg-color` | `var(
    --button-text-color-primary,
    light-dark(#fbfbfe` / `var(--button-text-color-primary, ButtonFace)` |
| `--button-primary-hover-bg-color` | `var(
    --button-background-color-primary-hover,
    light-` / `var(
      --button-background-color-primary-hover,
      Se` |
| `--button-primary-hover-border-color` | `var(--button-primary-hover-bg-color)` / `var(
      --button-border-color-primary-hover,
      Select` |
| `--button-primary-hover-fg-color` | `var(--button-primary-fg-color)` / `var(
      --button-text-color-primary-hover,
      Highligh` |
| `--button-secondary-active-bg-color` | `var(
    --button-background-color-active,
    light-dark(rg` / `var(
      --button-background-color-active,
      Highlight` |
| `--button-secondary-active-border-color` | `var(--button-secondary-bg-color)` / `var(
      --button-border-color-active,
      ButtonText
  ` |
| `--button-secondary-active-fg-color` | `var(--button-secondary-fg-color)` / `var(
      --button-text-color-active,
      SelectedItem
  ` |
| `--button-secondary-bg-color` | `var(
    --button-background-color,
    light-dark(rgb(21 20` / `var(--button-background-color, ButtonFace)` |
| `--button-secondary-border-color` | `var(
    --button-border-color,
    var(--button-secondary-b` / `var(--button-border-color, ButtonText)` |
| `--button-secondary-disabled-bg-color` | `var(--button-secondary-bg-color)` |
| `--button-secondary-disabled-border-color` | `var(
    --button-secondary-border-color
  )` / `var(
      --button-border-color-disabled,
      GrayText
  ` |
| `--button-secondary-disabled-fg-color` | `var(--button-secondary-fg-color)` / `var(
      --button-text-color-disabled,
      GrayText
    ` |
| `--button-secondary-fg-color` | `var(--text-color, light-dark(#15141a, #fbfbfe))` / `var(--button-text-color, ButtonText)` |
| `--button-secondary-hover-bg-color` | `var(
    --button-background-color-hover,
    light-dark(rgb` / `var(
      --button-background-color-hover,
      HighlightT` |
| `--button-secondary-hover-border-color` | `var(--button-secondary-hover-bg-color)` / `var(
      --button-border-color-hover,
      SelectedItem
 ` |
| `--button-secondary-hover-fg-color` | `var(--button-secondary-fg-color)` / `var(
      --button-text-color-hover,
      SelectedItem
   ` |
| `--button-signature-active-bg` | `light-dark(#cfcfd8, #5b5b66)` / `ButtonText` |
| `--button-signature-active-border` | `none` |
| `--button-signature-active-color` | `var(--button-signature-color)` / `HighlightText` |
| `--button-signature-bg` | `transparent` / `HighlightText` |
| `--button-signature-border` | `none` / `1px solid ButtonText` |
| `--button-signature-color` | `var(--main-color)` / `ButtonText` |
| `--button-signature-hover-bg` | `light-dark(#e0e0e6, #52525e)` / `Highlight` |
| `--button-signature-hover-color` | `var(--button-signature-color)` / `HighlightText` |
| `--can-scroll-left-NTZcf6` | `before,.studio-inline-reference-upload__scroll-content--can-` / `before{background:-moz-linear-gradient(left,#262626 0,rgba(3` |
| `--can-scroll-right-mvxVki` | `after{background:-moz-linear-gradient(right,#262626 0,rgba(3` |
| `--canvas-agent-loading-radius` | `8px` |
| `--canvas-card-overlay-enter-offset` | `30px` / `-30px` |
| `--canvas-connection-hover-color` | `hsla(0,0%,100%,.48)` |
| `--canvas-connection-target-shadow-x` | `0px` |
| `--canvas-connection-target-shadow-y` | `0px` |
| `--canvas-connection-target-tilt-x` | `0deg` |
| `--canvas-connection-target-tilt-y` | `0deg` |
| `--canvas-node-media-bleed` | `-moz-calc(1px*var(--canvas-node-outline-scale,1))` / `calc(1px*var(--canvas-node-outline-scale, 1))` |
| `--clear-button-icon` | `url(images/messageBar_closingButton.svg)` |
| `--clear-signature-button-icon` | `url(images/editor-toolbar-delete.svg)` |
| `--close-button-icon` | `url(images/pages_closeButton.svg)` |
| `--closing-button-icon` | `url(images/messageBar_closingButton.svg)` |
| `--code-bg` | `var(--skill-code-bg,#191c1f)` |
| `--collab-edit-color` | `#2563eb` / `#dc2626` / `#16a34a` |
| `--color-bg-1` | `#fff` / `#17171a` |
| `--color-bg-2` | `#fff` / `#232324` |
| `--color-bg-3` | `#fff` / `#2a2a2b` |
| `--color-bg-4` | `#fff` / `#313132` |
| `--color-bg-5` | `#fff` / `#373739` |
| `--color-bg-popup` | `#070709` / `var(--color-bg-5)` |
| `--color-bg-white` | `#fff` / `#f6f6f6` |
| `--color-black` | `#000` |
| `--color-border` | `rgb(var(--gray-3))` / `#333335` |
| `--color-border-1` | `var(--color-neutral-2)` |
| `--color-border-2` | `var(--color-neutral-3)` |
| `--color-border-3` | `var(--color-neutral-4)` |
| `--color-border-4` | `var(--color-neutral-6)` |
| `--color-danger-light-1` | `rgb(var(--danger-1))` / `rgba(var(--danger-6),0.2)` |
| `--color-danger-light-2` | `rgb(var(--danger-2))` / `rgba(var(--danger-6),0.35)` |
| `--color-danger-light-3` | `rgb(var(--danger-3))` / `rgba(var(--danger-6),0.5)` |
| `--color-danger-light-4` | `rgb(var(--danger-4))` / `rgba(var(--danger-6),0.65)` |
| `--color-fill-1` | `var(--color-neutral-1)` / `hsla(0,0%,100%,.04)` |
| `--color-fill-2` | `var(--color-neutral-2)` / `hsla(0,0%,100%,.08)` |
| `--color-fill-3` | `var(--color-neutral-3)` / `hsla(0,0%,100%,.12)` |
| `--color-fill-4` | `var(--color-neutral-4)` / `hsla(0,0%,100%,.16)` |
| `--color-link-light-1` | `rgb(var(--link-1))` / `rgba(var(--link-6),0.2)` |
| `--color-link-light-2` | `rgb(var(--link-2))` / `rgba(var(--link-6),0.35)` |
| `--color-link-light-3` | `rgb(var(--link-3))` / `rgba(var(--link-6),0.5)` |
| `--color-link-light-4` | `rgb(var(--link-4))` / `rgba(var(--link-6),0.65)` |
| `--color-mask-bg` | `rgba(29,33,41,.6)` / `rgba(23,23,26,.6)` |
| `--color-menu-dark-bg` | `#232324` |
| `--color-menu-dark-hover` | `hsla(0,0%,100%,.04)` / `var(--color-fill-2)` |
| `--color-menu-light-bg` | `#fff` / `#232324` |
| `--color-neutral-1` | `rgb(var(--gray-1))` |
| `--color-neutral-10` | `rgb(var(--gray-10))` |
| `--color-neutral-2` | `rgb(var(--gray-2))` |
| `--color-neutral-3` | `rgb(var(--gray-3))` |
| `--color-neutral-4` | `rgb(var(--gray-4))` |
| `--color-neutral-5` | `rgb(var(--gray-5))` |
| `--color-neutral-6` | `rgb(var(--gray-6))` |
| `--color-neutral-7` | `rgb(var(--gray-7))` |
| `--color-neutral-8` | `rgb(var(--gray-8))` |
| `--color-neutral-9` | `rgb(var(--gray-9))` |
| `--color-primary-light-1` | `rgb(var(--primary-1))` / `rgba(var(--primary-6),0.2)` |
| `--color-primary-light-2` | `rgb(var(--primary-2))` / `rgba(var(--primary-6),0.35)` |
| `--color-primary-light-3` | `rgb(var(--primary-3))` / `rgba(var(--primary-6),0.5)` |
| `--color-primary-light-4` | `rgb(var(--primary-4))` / `rgba(var(--primary-6),0.65)` |
| `--color-secondary` | `var(--color-neutral-2)` / `rgba(var(--gray-9),0.08)` |
| `--color-secondary-active` | `var(--color-neutral-4)` / `rgba(var(--gray-7),0.24)` |
| `--color-secondary-disabled` | `var(--color-neutral-1)` / `rgba(var(--gray-9),0.08)` |
| `--color-secondary-hover` | `var(--color-neutral-3)` / `rgba(var(--gray-8),0.16)` |
| `--color-spin-layer-bg` | `hsla(0,0%,100%,.6)` / `rgba(51,51,51,.6)` |
| `--color-success-light-1` | `rgb(var(--success-1))` / `rgba(var(--success-6),0.2)` |
| `--color-success-light-2` | `rgb(var(--success-2))` / `rgba(var(--success-6),0.35)` |
| `--color-success-light-3` | `rgb(var(--success-3))` / `rgba(var(--success-6),0.5)` |
| `--color-success-light-4` | `rgb(var(--success-4))` / `rgba(var(--success-6),0.65)` |
| `--color-text-1` | `var(--grey-5)` / `var(--color-neutral-10)` / `hsla(0,0%,100%,.9)` |
| `--color-text-2` | `var(--grey-3)` / `var(--color-neutral-8)` / `hsla(0,0%,100%,.7)` |
| `--color-text-3` | `var(--color-neutral-6)` / `hsla(0,0%,100%,.5)` |
| `--color-text-4` | `var(--color-neutral-4)` / `hsla(0,0%,100%,.3)` |
| `--color-tooltip-bg` | `rgb(var(--gray-10))` / `#373739` |
| `--color-warning-light-1` | `rgb(var(--warning-1))` / `rgba(var(--warning-6),0.2)` |
| `--color-warning-light-2` | `rgb(var(--warning-2))` / `rgba(var(--warning-6),0.35)` |
| `--color-warning-light-3` | `rgb(var(--warning-3))` / `rgba(var(--warning-6),0.5)` |
| `--color-warning-light-4` | `rgb(var(--warning-4))` / `rgba(var(--warning-6),0.65)` |
| `--color-white` | `#fff` / `hsla(0,0%,100%,.9)` |
| `--comb-letter-spacing` | `calc(var(--comb-width) - 1ch)` |
| `--comb-width` | `0px` |
| `--comment-active-bg-color` | `light-dark(#d1d1d9, #3a3944)` / `Canvas` |
| `--comment-active-brightness` | `0.825` |
| `--comment-active-filter` | `brightness(var(--comment-active-brightness))` / `none` |
| `--comment-bg-color` | `light-dark(#f9f9fb, #1c1b22)` / `Canvas` |
| `--comment-border-color` | `light-dark(#f0f0f4, #52525e)` / `CanvasText` |
| `--comment-button-active-bg` | `light-dark(#0041a4, #a6ecf4)` / `var(
        --button-background-color-active,
        Selec` |
| `--comment-button-active-border-color` | `var(--comment-button-active-bg)` / `var(
        --button-border-color-active,
        ButtonBor` |
| `--comment-button-active-fg` | `var(
      --button-text-color-primary,
      light-dark(whi` / `var(--button-text-color-active, SelectedItem)` |
| `--comment-button-bg` | `var(
      --background-color-canvas,
      light-dark(white` / `var(--button-background-color, ButtonFace)` |
| `--comment-button-border-color` | `var(
      --border-color-interactive,
      light-dark(#8f8` / `var(--button-border-color, ButtonBorder)` |
| `--comment-button-box-shadow` | `0 0.25px 0.75px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / ` / `none` |
| `--comment-button-dim` | `24px` |
| `--comment-button-fg` | `light-dark(#5b5b66, #fbfbfe)` / `var(--button-text-color, ButtonText)` |
| `--comment-button-focus-border-color` | `light-dark(#cfcfd8, #3a3944)` |
| `--comment-button-focus-outline-color` | `var(
      --focus-outline-color,
      light-dark(#0062fa, ` / `var(
        --focus-outline-color,
        CanvasText
     ` |
| `--comment-button-hover-bg` | `var(
      --color-accent-primary-hover,
      light-dark(#0` / `var(
        --button-background-color-hover,
        Select` |
| `--comment-button-hover-border-color` | `var(--comment-button-hover-bg)` / `var(
        --button-border-color-hover,
        SelectedIt` |
| `--comment-button-hover-fg` | `var(
      --button-text-color-primary,
      light-dark(whi` / `var(--button-text-color-hover, SelectedItem)` |
| `--comment-button-selected-bg` | `var(
      --color-accent-primary,
      light-dark(#0062fa,` / `var(
        --button-background-color-primary,
        Butt` |
| `--comment-button-selected-border-color` | `var(--comment-button-selected-bg)` |
| `--comment-button-selected-fg` | `var(
      --button-text-color-primary,
      light-dark(whi` / `var(
        --button-text-color-primary,
        ButtonFace` |
| `--comment-close-button-icon` | `url(images/comment-closeButton.svg)` |
| `--comment-count-bg-color` | `light-dark(#e2f7ff, #00317e)` / `Canvas` |
| `--comment-date-fg-color` | `light-dark(
    rgb(21 20 26 / 0.69),
    rgb(251 251 254 / ` / `CanvasText` |
| `--comment-fg-color` | `var(--text-color, light-dark(#15141a, #fbfbfe))` / `var(--text-color, CanvasText)` |
| `--comment-focus-outline-color` | `var(
    --focus-outline-color,
    light-dark(#0062fa, #00c` |
| `--comment-hover-bg-color` | `light-dark(#e0e0e6, #2c2b33)` / `Canvas` |
| `--comment-hover-brightness` | `0.89` |
| `--comment-hover-filter` | `brightness(var(--comment-hover-brightness))` / `none` |
| `--comment-indicator-active-fg-color` | `light-dark(#0041a4, #a6ecf4)` / `SelectedItem` |
| `--comment-indicator-active-filter` | `brightness(
    calc(1 / var(--comment-active-brightness))
 ` |
| `--comment-indicator-focus-fg-color` | `light-dark(#5b5b66, #fbfbfe)` / `var(--text-color, CanvasText)` |
| `--comment-indicator-hover-fg-color` | `var(
    --color-accent-primary-hover,
    light-dark(#0053c` / `var(--text-color, CanvasText)` |
| `--comment-indicator-hover-filter` | `brightness(
    calc(1 / var(--comment-hover-brightness))
  ` |
| `--comment-indicator-selected-fg-color` | `var(
    --color-accent-primary,
    light-dark(#0062fa, #00` / `SelectedItem` |
| `--comment-popup-delete-button-icon` | `url(images/editor-toolbar-delete.svg)` |
| `--comment-popup-edit-button-icon` | `url(images/comment-popup-editButton.svg)` |
| `--comment-shadow` | `0 0.5px 2px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / 0.2)` / `none` |
| `--composer-bg` | `var(--skill-composer-bg,#272a2d)` |
| `--composer-shadow` | `var(--skill-composer-shadow,0 4px 16px #0002)` |
| `--control-line` | `var(--skill-control-line,#ffffff1f)` |
| `--conversation-width` | `904px` / `1200px` / `100%` |
| `--current-outline-button-icon` | `url(images/toolbarButton-currentOutlineItem.svg)` |
| `--cyan-0` | `#213539` |
| `--cyan-1` | `#004d52` / `232,255,251` / `0,66,77` |
| `--cyan-10` | `0,66,77` / `240,255,252` |
| `--cyan-2` | `#00c1cd` / `183,244,236` / `6,97,108` |
| `--cyan-2-rgb` | `0,193,205` |
| `--cyan-3` | `#33cdd7` / `137,233,224` / `17,131,139` |
| `--cyan-4` | `94,223,214` / `31,166,170` |
| `--cyan-5` | `55,212,207` / `48,201,201` |
| `--cyan-6` | `20,201,201` / `63,212,207` |
| `--cyan-7` | `13,165,170` / `102,223,215` |
| `--cyan-8` | `7,130,139` / `144,233,225` |
| `--cyan-9` | `3,97,108` / `190,244,237` |
| `--danger` | `var(--skill-danger,#e7a6a6)` |
| `--danger-1` | `var(--red-1)` |
| `--danger-10` | `var(--red-10)` |
| `--danger-2` | `var(--red-2)` |
| `--danger-3` | `var(--red-3)` |
| `--danger-4` | `var(--red-4)` |
| `--danger-5` | `var(--red-5)` |
| `--danger-6` | `var(--red-6)` |
| `--danger-7` | `var(--red-7)` |
| `--danger-8` | `var(--red-8)` |
| `--danger-9` | `var(--red-9)` |
| `--dialog-bg-color` | `var(--background-color-canvas, light-dark(white, #1c1b22))` / `var(--background-color-canvas, Canvas)` |
| `--dialog-border-color` | `var(
    --background-color-canvas,
    light-dark(white, #1` / `var(--border-color, CanvasText)` |
| `--dialog-shadow` | `0 2px 14px 0 light-dark(rgb(58 57 68 / 0.2), #15141a)` / `none` |
| `--diff-add-bg` | `var(--skill-diff-add-bg,#20372c)` |
| `--diff-remove-bg` | `var(--skill-diff-remove-bg,#3c282c)` |
| `--disabled-opacity` | `0.62` / `1` |
| `--divider-color` | `CanvasText` / `light-dark(#cfcfd8, #3a3944)` / `light-dark(#d7d7db, #8f8f9d)` |
| `--draw-cursor` | `url(images/cursor-editorInk.svg) 0 16, pointer` |
| `--editor-selection-outline` | `solid var(--outline-width) var(--outline-color)` |
| `--editor-toolbar-bg-color` | `light-dark(#f0f0f4, #2b2a33)` / `var(--button-background-color, ButtonFace)` |
| `--editor-toolbar-border-color` | `var(--border-color-interactive, #8f8f9d)` / `var(--button-border-color, ButtonText)` |
| `--editor-toolbar-colorpicker-arrow-image` | `url(images/toolbarButton-menuArrow.svg)` |
| `--editor-toolbar-delete-image` | `url(images/editor-toolbar-delete.svg)` |
| `--editor-toolbar-fg-color` | `light-dark(#2e2e56, #fbfbfe)` / `var(--button-text-color, ButtonText)` |
| `--editor-toolbar-focus-outline-color` | `var(
      --focus-outline-color,
      light-dark(#0060df, ` / `var(
        --button-border-color,
        ButtonBorder
   ` |
| `--editor-toolbar-height` | `28px` |
| `--editor-toolbar-highlight-image` | `url(images/toolbarButton-editorHighlight.svg)` |
| `--editor-toolbar-hover-bg-color` | `light-dark(#e0e0e6, #52525e)` / `var(
        --button-background-color-hover,
        Button` |
| `--editor-toolbar-hover-border-color` | `var(--editor-toolbar-border-color)` / `var(
        --button-border-color-hover,
        AccentColo` |
| `--editor-toolbar-hover-fg-color` | `var(--editor-toolbar-fg-color)` / `var(
        --button-text-color-hover,
        AccentColor
` |
| `--editor-toolbar-hover-outline` | `none` / `2px solid var(--editor-toolbar-hover-border-color)` |
| `--editor-toolbar-padding` | `2px` |
| `--editor-toolbar-shadow` | `0 2px 6px 0 rgb(58 57 68 / 0.2)` / `none` |
| `--editor-toolbar-vert-offset` | `6px` |
| `--editorFreeHighlight-editing-cursor` | `url(images/cursor-editorFreeHighlight.svg) 1 18, pointer` |
| `--editorFreeText-editing-cursor` | `text` / `url(images/cursor-editorFreeText.svg) 0 16, text` |
| `--editorHighlight-editing-cursor` | `url(images/cursor-editorTextHighlight.svg) 24 24, text` |
| `--editorInk-editing-cursor` | `url(images/cursor-editorInk.svg) 0 16, pointer` |
| `--example-color` | `light-dark(#bfbfc9, #80808e)` / `CanvasText` |
| `--flow-angle` | `290deg` |
| `--flow-canvas-edge` | `#555e60` |
| `--flow-canvas-edge-selected` | `#62d9df` |
| `--flow-canvas-transfer-blocked-opacity` | `0.3` |
| `--flow-canvas-transfer-connection-line` | `var(--canvas-connection-hover-color)` |
| `--flow-canvas-transfer-owner` | `transparent` |
| `--flow-end` | `0deg` |
| `--flow-solid-end` | `0deg` |
| `--flow-solid-start` | `0deg` |
| `--focus-outline-around` | `solid var(--outline-around-width) var(--outline-around-color` |
| `--focus-ring-color` | `var(--focus-outline-color, light-dark(#0060df, #0df))` / `var(--focus-outline-color, CanvasText)` |
| `--focus-ring-outline` | `var(--focus-outline-width, 2px) solid var(--focus-ring-color` |
| `--font-height` | `0` |
| `--frame-yQX27F` | `focus,.studio-inline-reference-upload--frame-mode-Abi4YF .st` |
| `--freetext-line-height` | `1.35` |
| `--freetext-padding` | `2px` |
| `--gap-between-input-and-thumbnail` | `16px` / `0px` |
| `--generating-PpYnTz` | `disabled{background:#f5f6ff` / `disabled:hover{background:#f5f6ff` |
| `--gold-1` | `255,252,232` / `77,45,0` |
| `--gold-10` | `77,45,0` / `255,252,232` |
| `--gold-2` | `253,244,191` / `119,75,4` |
| `--gold-3` | `252,233,150` / `162,111,15` |
| `--gold-4` | `250,220,109` / `204,150,31` |
| `--gold-5` | `249,204,69` / `247,192,52` |
| `--gold-6` | `247,186,30` / `249,204,68` |
| `--gold-7` | `204,146,19` / `250,220,108` |
| `--gold-8` | `162,109,10` / `252,233,149` |
| `--gold-9` | `119,75,4` / `253,244,190` |
| `--gray-1` | `247,248,250` / `23,23,26` |
| `--gray-10` | `29,33,41` / `246,246,246` |
| `--gray-2` | `242,243,245` / `46,46,48` |
| `--gray-3` | `229,230,235` / `72,72,73` |
| `--gray-4` | `201,205,212` / `95,95,96` |
| `--gray-5` | `169,174,184` / `120,120,122` |
| `--gray-6` | `134,144,156` / `146,146,147` |
| `--gray-7` | `107,119,133` / `171,171,172` |
| `--gray-8` | `78,89,105` / `197,197,197` |
| `--gray-9` | `39,46,59` / `223,223,223` |
| `--green-1` | `232,255,234` / `0,77,28` |
| `--green-10` | `0,77,28` / `235,255,236` |
| `--green-2` | `175,240,181` / `4,102,37` |
| `--green-3` | `123,225,136` / `10,128,45` |
| `--green-4` | `76,210,99` / `18,154,55` |
| `--green-5` | `35,195,67` / `29,180,64` |
| `--green-6` | `0,180,42` / `39,195,70` |
| `--green-7` | `0,154,41` / `80,210,102` |
| `--green-8` | `0,128,38` / `126,225,139` |
| `--green-9` | `0,102,34` / `178,240,183` |
| `--grey-0` | `#4c4c4c` |
| `--grey-0-rgb` | `76,76,76` |
| `--grey-1` | `#6c6c6c` |
| `--grey-1-rgb` | `108,108,108` |
| `--grey-2` | `grey` |
| `--grey-3` | `#999` |
| `--grey-5` | `#d4d4d4` |
| `--grey-6` | `#e5e5e5` |
| `--grey-7` | `#b2b2b2` |
| `--group-resize-arc-scale` | `-moz-calc(var(--canvas-node-radius-scale,1)*15/15 - var(--ca` / `calc(var(--canvas-node-radius-scale, 1)*15/15 - var(--canvas` |
| `--group-resize-half-border` | `-moz-calc(1px*var(--canvas-node-outline-scale,1)*0.5)` / `calc(1px*var(--canvas-node-outline-scale, 1)*0.5)` |
| `--group-resize-offset` | `-moz-calc(var(--node-resize-container-border-width,1px)*-1)` / `calc(var(--node-resize-container-border-width, 1px)*-1)` |
| `--guide-spark-shape` | `url("data:image/svg+xml` |
| `--hcm-highlight-filter` | `none` / `invert(100%)` |
| `--hcm-highlight-selected-filter` | `none` |
| `--header-bg` | `light-dark(rgb(255 255 255 / 0.92), #42414e)` |
| `--header-shadow` | `0 0.25px 0.75px -0.75px light-dark(rgb(0 0 0 / 0.05), rgb(0 ` / `none` |
| `--heycan-checkbox-line-height` | `16px` |
| `--heycan-form-field-label-color` | `var(--grey-5)` |
| `--heycan-form-field-label-line-height` | `16px` / `22px` |
| `--heycan-form-field-margin-inline-end` | `10px` |
| `--heycan-form-field-margin-top` | `8px` / `12px` / `16px` |
| `--heycan-form-field-vertical-padding` | `0` |
| `--heycan-input-background-color` | `var(--black-5)` |
| `--heycan-input-vertical-padding` | `0` / `5px` / `2px` |
| `--heycan-tag-grey-bg` | `var(--black-5)` / `var(--alpha-3w)` / `var(--black-4)` |
| `--heycan-textarea-background-color` | `var(--black-5)` |
| `--highlight-backdrop-filter` | `none` / `var(--hcm-highlight-filter)` |
| `--highlight-bg-color` | `rgb(180 0 170 / 0.25)` / `transparent` |
| `--highlight-selected-backdrop-filter` | `none` / `var(
        --hcm-highlight-selected-filter
      )` |
| `--highlight-selected-bg-color` | `rgb(0 100 0 / 0.25)` / `transparent` |
| `--history-selected` | `var(--skill-history-selected,#272a2d)` |
| `--hover` | `var(--skill-hover,#ffffff14)` |
| `--hover-filter` | `brightness(0.9)` / `brightness(1.4)` / `none` |
| `--hover-outline` | `solid var(--outline-width) var(--hover-outline-color)` |
| `--hover-outline-around` | `solid var(--outline-around-width) var(--hover-outline-around` |
| `--hover-outline-around-color` | `var(--outline-around-color)` / `SelectedItemText` |
| `--hover-outline-color` | `var(--color-gray-60, #8f8f9d)` / `var(--color-accent-primary-hover, Highlight)` / `var(
    --color-accent-primary-hover,
    light-dark(#0250b` |
| `--icon-bg` | `var(--skill-icon-bg,#ffffff0a)` |
| `--image-border-color` | `light-dark(#cfcfd8, #3a3944)` |
| `--image-border-width` | `6px` |
| `--image-current-border-color` | `var(--button-focus-outline-color)` / `var(--border-color, ButtonText)` |
| `--image-current-focused-outline-color` | `var(--image-hover-border-color)` |
| `--image-current-hover-page-number-bg` | `var(--image-current-page-number-bg)` / `SelectedItem` |
| `--image-current-hover-page-number-fg` | `var(--image-current-page-number-fg)` / `SelectedItemText` |
| `--image-current-page-number-bg` | `var(--image-current-border-color)` / `ButtonText` |
| `--image-current-page-number-fg` | `light-dark(#fff, #15141a)` / `ButtonFace` |
| `--image-current-shadow` | `0 0.375px 1.5px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / ` |
| `--image-dragging-placeholder-bg` | `light-dark(
    rgb(0 98 250 / 0.08),
    rgb(0 202 219 / 0.` / `Canvas` |
| `--image-dragging-placeholder-border` | `var(--image-outline)` / `1px GrayText solid` |
| `--image-dragging-shadow` | `0 0 0 var(--image-border-width) var(--image-current-border-c` |
| `--image-focus-outline-color` | `CanvasText` |
| `--image-hover-border-color` | `#bfbfc9` / `SelectedItem` |
| `--image-hover-page-number-bg` | `var(--image-page-number-bg)` / `SelectedItemText` |
| `--image-hover-page-number-fg` | `var(--image-page-number-fg)` / `SelectedItem` |
| `--image-hover-shadow` | `0 0.375px 1.5px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / ` |
| `--image-multiple-dragging-shadow` | `0 0 0 var(--image-border-width) var(--image-current-border-c` |
| `--image-outline` | `none` / `1px solid ButtonText` |
| `--image-page-number-bg` | `light-dark(#f0f0f4, #42414d)` / `ButtonFace` |
| `--image-page-number-border-color` | `transparent` / `var(--image-page-number-fg)` |
| `--image-page-number-fg` | `var(--views-text-color)` / `ButtonText` |
| `--image-shadow` | `0 0.375px 1.5px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / ` / `none` |
| `--indicator-color` | `var(--color-accent-primary, light-dark(#0062fa, #00cadb))` / `var(--text-color, CanvasText)` |
| `--indicator-warning-color` | `light-dark(#b20037, #ffa0aa)` / `CanvasText` |
| `--indigo-0` | `#505057` |
| `--indigo-1` | `#676770` |
| `--indigo-2` | `#737379` |
| `--indigo-5` | `#c5c5d6` |
| `--input-dim` | `16px` / `0px` |
| `--input-disabled-border-color` | `transparent` / `GrayText` |
| `--input-focus-border-color` | `Highlight` / `CanvasText` |
| `--input-focus-outline` | `1px solid Canvas` |
| `--input-hover-border-color` | `black` / `Highlight` |
| `--input-text-bg-color` | `light-dark(white, #42414d)` / `Field` |
| `--input-text-fg-color` | `var(--text-primary-color)` / `FieldText` |
| `--input-unfocused-border-color` | `transparent` / `ActiveText` |
| `--input-width` | `var(--toggle-width)` |
| `--lime-1` | `252,255,232` / `42,77,0` |
| `--lime-10` | `42,77,0` / `253,255,238` |
| `--lime-2` | `237,248,187` / `68,112,6` |
| `--lime-3` | `220,241,144` / `98,148,18` |
| `--lime-4` | `201,233,104` / `132,183,35` |
| `--lime-5` | `181,226,65` / `168,219,57` |
| `--lime-6` | `159,219,29` / `184,226,75` |
| `--lime-7` | `126,183,18` / `203,233,112` |
| `--lime-8` | `95,148,10` / `222,241,152` |
| `--lime-9` | `67,112,4` / `238,248,194` |
| `--line` | `var(--skill-line,#ffffff0f)` |
| `--link-1` | `var(--arcoblue-1)` |
| `--link-10` | `var(--arcoblue-10)` |
| `--link-2` | `var(--arcoblue-2)` |
| `--link-3` | `var(--arcoblue-3)` |
| `--link-4` | `var(--arcoblue-4)` |
| `--link-5` | `var(--arcoblue-5)` |
| `--link-6` | `var(--arcoblue-6)` |
| `--link-7` | `var(--arcoblue-7)` |
| `--link-8` | `var(--arcoblue-8)` |
| `--link-9` | `var(--arcoblue-9)` |
| `--link-fg-color` | `var(--link-color, light-dark(#0060df, #0df))` / `var(--link-color, LinkText)` |
| `--link-hover-fg-color` | `var(--link-color-hover, light-dark(#0250bb, #80ebff))` / `var(--link-color-hover, LinkText)` |
| `--link-outline` | `none` / `1.5px solid LinkText` |
| `--loading-icon-delay` | `400ms` |
| `--logo-shimmer-mask` | `url("data:image/svg+xml` |
| `--lv-arcoblue-1` | `232,243,255` / `0,13,77` |
| `--lv-arcoblue-10` | `0,13,77` / `234,244,255` |
| `--lv-arcoblue-2` | `190,218,255` / `4,27,121` |
| `--lv-arcoblue-3` | `148,191,255` / `14,50,166` |
| `--lv-arcoblue-4` | `106,161,255` / `29,77,210` |
| `--lv-arcoblue-5` | `64,128,255` / `48,111,255` |
| `--lv-arcoblue-6` | `22,93,255` / `60,126,255` |
| `--lv-arcoblue-7` | `14,66,210` / `104,159,255` |
| `--lv-arcoblue-8` | `7,44,166` / `147,190,255` |
| `--lv-arcoblue-9` | `3,26,121` / `190,218,255` |
| `--lv-blue-1` | `232,247,255` / `0,26,77` |
| `--lv-blue-10` | `0,26,77` / `234,248,255` |
| `--lv-blue-2` | `195,231,254` / `5,47,120` |
| `--lv-blue-3` | `159,212,253` / `19,76,163` |
| `--lv-blue-4` | `123,192,252` / `41,113,207` |
| `--lv-blue-5` | `87,169,251` / `70,154,250` |
| `--lv-blue-6` | `52,145,250` / `90,170,251` |
| `--lv-blue-7` | `32,108,207` / `125,193,252` |
| `--lv-blue-8` | `17,75,163` / `161,213,253` |
| `--lv-blue-9` | `6,48,120` / `198,232,254` |
| `--lv-border-radius-circle` | `50%` |
| `--lv-border-radius-large` | `8px` |
| `--lv-border-radius-medium` | `4px` |
| `--lv-border-radius-none` | `0` |
| `--lv-border-radius-small` | `2px` |
| `--lv-color-bg-5` | `#fff` / `#373739` |
| `--lv-color-bg-popup` | `var(--lv-color-bg-5)` |
| `--lv-color-bg-white` | `#fff` / `#f6f6f6` |
| `--lv-color-black` | `#000` |
| `--lv-color-border` | `rgb(var(--lv-gray-3))` / `#333335` |
| `--lv-color-border-1` | `var(--lv-color-neutral-2)` |
| `--lv-color-border-2` | `var(--lv-color-neutral-3)` |
| `--lv-color-border-3` | `var(--lv-color-neutral-4)` |
| `--lv-color-border-4` | `var(--lv-color-neutral-6)` |
| `--lv-color-danger-light-1` | `rgb(var(--lv-danger-1))` / `rgba(var(--lv-danger-6),.2)` / `rgba(var(--lv-danger-6),0.2)` |
| `--lv-color-danger-light-2` | `rgb(var(--lv-danger-2))` / `rgba(var(--lv-danger-6),.35)` / `rgba(var(--lv-danger-6),0.35)` |
| `--lv-color-danger-light-3` | `rgb(var(--lv-danger-3))` / `rgba(var(--lv-danger-6),.5)` / `rgba(var(--lv-danger-6),0.5)` |
| `--lv-color-danger-light-4` | `rgb(var(--lv-danger-4))` / `rgba(var(--lv-danger-6),.65)` / `rgba(var(--lv-danger-6),0.65)` |
| `--lv-color-fill-1` | `var(--lv-color-neutral-1)` / `#ffffff0a` / `hsla(0,0%,100%,.04)` |
| `--lv-color-fill-2` | `var(--lv-color-neutral-2)` / `#ffffff14` / `hsla(0,0%,100%,.08)` |
| `--lv-color-fill-3` | `var(--lv-color-neutral-3)` / `#ffffff1f` / `hsla(0,0%,100%,.12)` |
| `--lv-color-fill-4` | `var(--lv-color-neutral-4)` / `#ffffff29` / `hsla(0,0%,100%,.16)` |
| `--lv-color-fill-bg-1` | `#fff` / `#17171a` |
| `--lv-color-fill-bg-2` | `#fff` / `#232324` |
| `--lv-color-fill-bg-3` | `#fff` / `#2a2a2b` |
| `--lv-color-fill-bg-4` | `#fff` / `#313132` |
| `--lv-color-link-light-1` | `rgb(var(--lv-link-1))` / `rgba(var(--lv-link-6),.2)` / `rgba(var(--lv-link-6),0.2)` |
| `--lv-color-link-light-2` | `rgb(var(--lv-link-2))` / `rgba(var(--lv-link-6),.35)` / `rgba(var(--lv-link-6),0.35)` |
| `--lv-color-link-light-3` | `rgb(var(--lv-link-3))` / `rgba(var(--lv-link-6),.5)` / `rgba(var(--lv-link-6),0.5)` |
| `--lv-color-link-light-4` | `rgb(var(--lv-link-4))` / `rgba(var(--lv-link-6),.65)` / `rgba(var(--lv-link-6),0.65)` |
| `--lv-color-mask-bg` | `#1d212999` / `#17171a99` / `rgba(29,33,41,.6)` |
| `--lv-color-menu-dark-bg` | `#232324` |
| `--lv-color-menu-dark-hover` | `var(--lv-color-fill-2)` / `#ffffff0a` / `hsla(0,0%,100%,.04)` |
| `--lv-color-menu-light-bg` | `#fff` / `#232324` |
| `--lv-color-neutral-1` | `rgb(var(--lv-gray-1))` |
| `--lv-color-neutral-10` | `rgb(var(--lv-gray-10))` |
| `--lv-color-neutral-2` | `rgb(var(--lv-gray-2))` |
| `--lv-color-neutral-3` | `rgb(var(--lv-gray-3))` |
| `--lv-color-neutral-4` | `rgb(var(--lv-gray-4))` |
| `--lv-color-neutral-5` | `rgb(var(--lv-gray-5))` |
| `--lv-color-neutral-6` | `rgb(var(--lv-gray-6))` |
| `--lv-color-neutral-7` | `rgb(var(--lv-gray-7))` |
| `--lv-color-neutral-8` | `rgb(var(--lv-gray-8))` |
| `--lv-color-neutral-9` | `rgb(var(--lv-gray-9))` |
| `--lv-color-primary-light-1` | `rgb(var(--lv-primary-1))` / `rgba(var(--lv-primary-6),.2)` / `rgba(var(--lv-primary-6),0.2)` |
| `--lv-color-primary-light-2` | `rgb(var(--lv-primary-2))` / `rgba(var(--lv-primary-6),.35)` / `rgba(var(--lv-primary-6),0.35)` |
| `--lv-color-primary-light-3` | `rgb(var(--lv-primary-3))` / `rgba(var(--lv-primary-6),.5)` / `rgba(var(--lv-primary-6),0.5)` |
| `--lv-color-primary-light-4` | `rgb(var(--lv-primary-4))` / `rgba(var(--lv-primary-6),.65)` / `rgba(var(--lv-primary-6),0.65)` |
| `--lv-color-secondary` | `var(--lv-color-neutral-2)` / `rgba(var(--lv-gray-9),.08)` / `rgba(var(--lv-gray-9),0.08)` |
| `--lv-color-secondary-active` | `var(--lv-color-neutral-4)` / `rgba(var(--lv-gray-7),.24)` / `rgba(var(--lv-gray-7),0.24)` |
| `--lv-color-secondary-disabled` | `var(--lv-color-neutral-1)` / `rgba(var(--lv-gray-9),.08)` / `rgba(var(--lv-gray-9),0.08)` |
| `--lv-color-secondary-hover` | `var(--lv-color-neutral-3)` / `rgba(var(--lv-gray-8),.16)` / `rgba(var(--lv-gray-8),0.16)` |
| `--lv-color-spin-layer-bg` | `#fff9` / `#3339` / `hsla(0,0%,100%,.6)` |
| `--lv-color-success-light-1` | `rgb(var(--lv-success-1))` / `rgba(var(--lv-success-6),.2)` / `rgba(var(--lv-success-6),0.2)` |
| `--lv-color-success-light-2` | `rgb(var(--lv-success-2))` / `rgba(var(--lv-success-6),.35)` / `rgba(var(--lv-success-6),0.35)` |
| `--lv-color-success-light-3` | `rgb(var(--lv-success-3))` / `rgba(var(--lv-success-6),.5)` / `rgba(var(--lv-success-6),0.5)` |
| `--lv-color-success-light-4` | `rgb(var(--lv-success-4))` / `rgba(var(--lv-success-6),.65)` / `rgba(var(--lv-success-6),0.65)` |
| `--lv-color-text-placeholder` | `var(--lv-color-neutral-4)` / `#ffffff4d` / `hsla(0,0%,100%,.3)` |
| `--lv-color-text-primary` | `var(--lv-color-neutral-10)` / `#ffffffe6` / `hsla(0,0%,100%,.9)` |
| `--lv-color-text-secondary` | `var(--lv-color-neutral-8)` / `#ffffffb3` / `hsla(0,0%,100%,.7)` |
| `--lv-color-text-tertiary` | `var(--lv-color-neutral-6)` / `#ffffff80` / `hsla(0,0%,100%,.5)` |
| `--lv-color-tooltip-bg` | `rgb(var(--lv-gray-10))` / `#373739` |
| `--lv-color-warning-light-1` | `rgb(var(--lv-warning-1))` / `rgba(var(--lv-warning-6),.2)` / `rgba(var(--lv-warning-6),0.2)` |
| `--lv-color-warning-light-2` | `rgb(var(--lv-warning-2))` / `rgba(var(--lv-warning-6),.35)` / `rgba(var(--lv-warning-6),0.35)` |
| `--lv-color-warning-light-3` | `rgb(var(--lv-warning-3))` / `rgba(var(--lv-warning-6),.5)` / `rgba(var(--lv-warning-6),0.5)` |
| `--lv-color-warning-light-4` | `rgb(var(--lv-warning-4))` / `rgba(var(--lv-warning-6),.65)` / `rgba(var(--lv-warning-6),0.65)` |
| `--lv-color-white` | `#fff` / `#ffffffe6` / `hsla(0,0%,100%,.9)` |
| `--lv-cyan-1` | `232,255,251` / `0,66,77` |
| `--lv-cyan-10` | `0,66,77` / `240,255,252` |
| `--lv-cyan-2` | `183,244,236` / `6,97,108` |
| `--lv-cyan-3` | `137,233,224` / `17,131,139` |
| `--lv-cyan-4` | `94,223,214` / `31,166,170` |
| `--lv-cyan-5` | `55,212,207` / `48,201,201` |
| `--lv-cyan-6` | `20,201,201` / `63,212,207` |
| `--lv-cyan-7` | `13,165,170` / `102,223,215` |
| `--lv-cyan-8` | `7,130,139` / `144,233,225` |
| `--lv-cyan-9` | `3,97,108` / `190,244,237` |
| `--lv-danger-1` | `var(--lv-red-1)` |
| `--lv-danger-10` | `var(--lv-red-10)` |
| `--lv-danger-2` | `var(--lv-red-2)` |
| `--lv-danger-3` | `var(--lv-red-3)` |
| `--lv-danger-4` | `var(--lv-red-4)` |
| `--lv-danger-5` | `var(--lv-red-5)` |
| `--lv-danger-6` | `var(--lv-red-6)` |
| `--lv-danger-7` | `var(--lv-red-7)` |
| `--lv-danger-8` | `var(--lv-red-8)` |
| `--lv-danger-9` | `var(--lv-red-9)` |
| `--lv-gold-1` | `255,252,232` / `77,45,0` |
| `--lv-gold-10` | `77,45,0` / `255,252,232` |
| `--lv-gold-2` | `253,244,191` / `119,75,4` |
| `--lv-gold-3` | `252,233,150` / `162,111,15` |
| `--lv-gold-4` | `250,220,109` / `204,150,31` |
| `--lv-gold-5` | `249,204,69` / `247,192,52` |
| `--lv-gold-6` | `247,186,30` / `249,204,68` |
| `--lv-gold-7` | `204,146,19` / `250,220,108` |
| `--lv-gold-8` | `162,109,10` / `252,233,149` |
| `--lv-gold-9` | `119,75,4` / `253,244,190` |
| `--lv-gray-1` | `247,248,250` / `23,23,26` |
| `--lv-gray-10` | `29,33,41` / `246,246,246` |
| `--lv-gray-2` | `242,243,245` / `46,46,48` |
| `--lv-gray-3` | `229,230,235` / `72,72,73` |
| `--lv-gray-4` | `201,205,212` / `95,95,96` |
| `--lv-gray-5` | `169,174,184` / `120,120,122` |
| `--lv-gray-6` | `134,144,156` / `146,146,147` |
| `--lv-gray-7` | `107,119,133` / `171,171,172` |
| `--lv-gray-8` | `78,89,105` / `197,197,197` |
| `--lv-gray-9` | `39,46,59` / `223,223,223` |
| `--lv-green-1` | `232,255,234` / `0,77,28` |
| `--lv-green-10` | `0,77,28` / `235,255,236` |
| `--lv-green-2` | `175,240,181` / `4,102,37` |
| `--lv-green-3` | `123,225,136` / `10,128,45` |
| `--lv-green-4` | `76,210,99` / `18,154,55` |
| `--lv-green-5` | `35,195,67` / `29,180,64` |
| `--lv-green-6` | `0,180,42` / `39,195,70` |
| `--lv-green-7` | `0,154,41` / `80,210,102` |
| `--lv-green-8` | `0,128,38` / `126,225,139` |
| `--lv-green-9` | `0,102,34` / `178,240,183` |
| `--lv-lime-1` | `252,255,232` / `42,77,0` |
| `--lv-lime-10` | `42,77,0` / `253,255,238` |
| `--lv-lime-2` | `237,248,187` / `68,112,6` |
| `--lv-lime-3` | `220,241,144` / `98,148,18` |
| `--lv-lime-4` | `201,233,104` / `132,183,35` |
| `--lv-lime-5` | `181,226,65` / `168,219,57` |
| `--lv-lime-6` | `159,219,29` / `184,226,75` |
| `--lv-lime-7` | `126,183,18` / `203,233,112` |
| `--lv-lime-8` | `95,148,10` / `222,241,152` |
| `--lv-lime-9` | `67,112,4` / `238,248,194` |
| `--lv-link-1` | `var(--lv-arcoblue-1)` |
| `--lv-link-10` | `var(--lv-arcoblue-10)` |
| `--lv-link-2` | `var(--lv-arcoblue-2)` |
| `--lv-link-3` | `var(--lv-arcoblue-3)` |
| `--lv-link-4` | `var(--lv-arcoblue-4)` |
| `--lv-link-5` | `var(--lv-arcoblue-5)` |
| `--lv-link-6` | `var(--lv-arcoblue-6)` |
| `--lv-link-7` | `var(--lv-arcoblue-7)` |
| `--lv-link-8` | `var(--lv-arcoblue-8)` |
| `--lv-link-9` | `var(--lv-arcoblue-9)` |
| `--lv-magenta-1` | `255,232,241` / `77,0,52` |
| `--lv-magenta-10` | `77,0,52` / `255,232,241` |
| `--lv-magenta-2` | `253,194,219` / `119,8,80` |
| `--lv-magenta-3` | `251,157,199` / `161,23,108` |
| `--lv-magenta-4` | `249,121,183` / `203,43,136` |
| `--lv-magenta-5` | `247,84,168` / `245,69,166` |
| `--lv-magenta-6` | `245,49,157` / `247,86,169` |
| `--lv-magenta-7` | `203,30,131` / `249,122,184` |
| `--lv-magenta-8` | `161,16,105` / `251,158,200` |
| `--lv-magenta-9` | `119,6,79` / `253,195,219` |
| `--lv-orange-1` | `255,247,232` / `77,27,0` |
| `--lv-orange-10` | `77,27,0` / `255,247,232` |
| `--lv-orange-2` | `255,228,186` / `121,48,4` |
| `--lv-orange-3` | `255,207,139` / `166,75,10` |
| `--lv-orange-4` | `255,182,93` / `210,105,19` |
| `--lv-orange-5` | `255,154,46` / `255,141,31` |
| `--lv-orange-6` | `255,125,0` / `255,150,38` |
| `--lv-orange-7` | `210,95,0` / `255,179,87` |
| `--lv-orange-8` | `166,69,0` / `255,205,135` |
| `--lv-orange-9` | `121,46,0` / `255,227,184` |
| `--lv-orangered-1` | `255,243,232` / `77,14,0` |
| `--lv-orangered-10` | `77,14,0` / `255,244,235` |
| `--lv-orangered-2` | `253,221,195` / `119,30,5` |
| `--lv-orangered-3` | `252,197,159` / `162,55,20` |
| `--lv-orangered-4` | `250,172,123` / `204,87,41` |
| `--lv-orangered-5` | `249,144,87` / `247,126,69` |
| `--lv-orangered-6` | `247,114,52` / `249,146,90` |
| `--lv-orangered-7` | `204,81,32` / `250,173,125` |
| `--lv-orangered-8` | `162,53,17` / `252,198,161` |
| `--lv-orangered-9` | `119,31,6` / `253,222,197` |
| `--lv-pinkpurple-1` | `255,232,251` / `66,0,77` |
| `--lv-pinkpurple-10` | `66,0,77` / `255,242,253` |
| `--lv-pinkpurple-2` | `247,186,239` / `101,3,112` |
| `--lv-pinkpurple-3` | `240,142,230` / `138,13,147` |
| `--lv-pinkpurple-4` | `232,101,223` / `176,27,182` |
| `--lv-pinkpurple-5` | `225,62,219` / `217,46,217` |
| `--lv-pinkpurple-6` | `217,26,217` / `225,61,219` |
| `--lv-pinkpurple-7` | `176,16,182` / `232,102,223` |
| `--lv-pinkpurple-8` | `138,9,147` / `240,146,230` |
| `--lv-pinkpurple-9` | `101,3,112` / `247,193,240` |
| `--lv-primary-1` | `var(--lv-arcoblue-1)` |
| `--lv-primary-10` | `var(--lv-arcoblue-10)` |
| `--lv-primary-2` | `var(--lv-arcoblue-2)` |
| `--lv-primary-3` | `var(--lv-arcoblue-3)` |
| `--lv-primary-4` | `var(--lv-arcoblue-4)` |
| `--lv-primary-5` | `var(--lv-arcoblue-5)` |
| `--lv-primary-6` | `var(--lv-arcoblue-6)` |
| `--lv-primary-7` | `var(--lv-arcoblue-7)` |
| `--lv-primary-8` | `var(--lv-arcoblue-8)` |
| `--lv-primary-9` | `var(--lv-arcoblue-9)` |
| `--lv-purple-1` | `245,232,255` / `22,0,77` |
| `--lv-purple-10` | `22,0,77` / `247,237,255` |
| `--lv-purple-2` | `221,190,246` / `39,6,110` |
| `--lv-purple-3` | `195,150,237` / `62,19,143` |
| `--lv-purple-4` | `168,113,227` / `90,37,176` |
| `--lv-purple-5` | `141,78,218` / `123,61,209` |
| `--lv-purple-6` | `114,46,209` / `142,81,218` |
| `--lv-purple-7` | `85,29,176` / `169,116,227` |
| `--lv-purple-8` | `60,16,143` / `197,154,237` |
| `--lv-purple-9` | `39,6,110` / `223,194,246` |
| `--lv-red-1` | `255,236,232` / `77,0,10` |
| `--lv-red-10` | `77,0,10` / `255,240,236` |
| `--lv-red-2` | `253,205,197` / `119,6,17` |
| `--lv-red-3` | `251,172,163` / `161,22,31` |
| `--lv-red-4` | `249,137,129` / `203,46,52` |
| `--lv-red-5` | `247,101,96` / `245,78,78` |
| `--lv-red-6` | `245,63,63` / `247,105,101` |
| `--lv-red-7` | `203,39,45` / `249,141,134` |
| `--lv-red-8` | `161,21,30` / `251,176,167` |
| `--lv-red-9` | `119,8,19` / `253,209,202` |
| `--lv-success-1` | `var(--lv-green-1)` |
| `--lv-success-10` | `var(--lv-green-10)` |
| `--lv-success-2` | `var(--lv-green-2)` |
| `--lv-success-3` | `var(--lv-green-3)` |
| `--lv-success-4` | `var(--lv-green-4)` |
| `--lv-success-5` | `var(--lv-green-5)` |
| `--lv-success-6` | `var(--lv-green-6)` |
| `--lv-success-7` | `var(--lv-green-7)` |
| `--lv-success-8` | `var(--lv-green-8)` |
| `--lv-success-9` | `var(--lv-green-9)` |
| `--lv-warning-1` | `var(--lv-orange-1)` |
| `--lv-warning-10` | `var(--lv-orange-10)` |
| `--lv-warning-2` | `var(--lv-orange-2)` |
| `--lv-warning-3` | `var(--lv-orange-3)` |
| `--lv-warning-4` | `var(--lv-orange-4)` |
| `--lv-warning-5` | `var(--lv-orange-5)` |
| `--lv-warning-6` | `var(--lv-orange-6)` |
| `--lv-warning-7` | `var(--lv-orange-7)` |
| `--lv-warning-8` | `var(--lv-orange-8)` |
| `--lv-warning-9` | `var(--lv-orange-9)` |
| `--lv-yellow-1` | `254,255,232` / `77,56,0` |
| `--lv-yellow-10` | `77,56,0` / `254,255,240` |
| `--lv-yellow-2` | `254,254,190` / `120,94,7` |
| `--lv-yellow-3` | `253,250,148` / `163,134,20` |
| `--lv-yellow-4` | `252,242,107` / `207,179,37` |
| `--lv-yellow-5` | `251,232,66` / `250,225,60` |
| `--lv-yellow-6` | `250,220,25` / `251,233,75` |
| `--lv-yellow-7` | `207,175,15` / `252,243,116` |
| `--lv-yellow-8` | `163,132,8` / `253,250,157` |
| `--lv-yellow-9` | `120,93,3` / `254,254,198` |
| `--lvv-border-radius-circle` | `50%` |
| `--lvv-border-radius-large` | `16px` |
| `--lvv-border-radius-medium` | `12px` |
| `--lvv-border-radius-none` | `0` |
| `--lvv-border-radius-small` | `8px` |
| `--lvv-border-radius-tiny` | `4px` |
| `--lvv-color-bg-1` | `#fff` / `#121217` |
| `--lvv-color-bg-2` | `#fafafa` / `#1c1c21` |
| `--lvv-color-bg-3` | `#f4f5f5` / `#28282e` |
| `--lvv-color-bg-4` | `#eeeff0` / `#303036` |
| `--lvv-color-bg-5` | `#e4e5e7` / `#43434c` |
| `--lvv-color-bg-6` | `#1e1e28` / `#f3f3f3` |
| `--lvv-color-bg-field` | `#0000000a` / `#ffffff0a` / `rgba(0,0,0,.04)` |
| `--lvv-color-bg-overlay` | `#fff` / `#1c1c21` |
| `--lvv-color-black-004` | `#0000000a` / `rgba(0,0,0,.04)` |
| `--lvv-color-black-006` | `#0000000f` / `rgba(0,0,0,.06)` |
| `--lvv-color-black-012` | `#0000001f` / `rgba(0,0,0,.12)` |
| `--lvv-color-black-02` | `#0003` / `rgba(0,0,0,.2)` / `var(--lvv-color-white-04,hsla(0,0%,100%,.4))` |
| `--lvv-color-black-025` | `#00000040` / `rgba(0,0,0,.25)` |
| `--lvv-color-black-04` | `#0006` / `rgba(0,0,0,.4)` |
| `--lvv-color-black-06` | `#0009` / `rgba(0,0,0,.6)` |
| `--lvv-color-black-08` | `#000c` / `rgba(0,0,0,.8)` |
| `--lvv-color-black-1` | `#0000000a` / `rgba(0,0,0,.04)` |
| `--lvv-color-black-2` | `#0000001f` / `rgba(0,0,0,.12)` |
| `--lvv-color-black-3` | `#0003` / `rgba(0,0,0,.2)` |
| `--lvv-color-black-4` | `#0006` / `rgba(0,0,0,.4)` |
| `--lvv-color-black-5` | `#0009` / `rgba(0,0,0,.6)` |
| `--lvv-color-black-6` | `#000c` / `rgba(0,0,0,.8)` |
| `--lvv-color-black-7` | `#000` |
| `--lvv-color-black-inverted` | `#000` / `#fff` |
| `--lvv-color-black-stationary` | `#000` |
| `--lvv-color-black-tooltip` | `#1e1e28` |
| `--lvv-color-common-blue-1` | `#5b8fff` |
| `--lvv-color-common-deep-purple-1` | `#7d5cff` |
| `--lvv-color-common-green-1` | `#00be93` |
| `--lvv-color-common-pink-1` | `#f75997` |
| `--lvv-color-common-pro-1` | `#caa06d` |
| `--lvv-color-common-purple-1` | `#b75cff` |
| `--lvv-color-common-red-1` | `#fc5d5b` |
| `--lvv-color-common-yellow-1` | `#ff832a` |
| `--lvv-color-fill-bg-1` | `#fff` / `#0e0e11` / `var(--panel-bg)` |
| `--lvv-color-fill-bg-2` | `#f2f5f7` / `#1c1d21` / `var(--page-bg)` |
| `--lvv-color-fill-bg-3` | `#eff3f5` / `#25262b` / `#edf0f5` |
| `--lvv-color-fill-bg-4` | `#ecf1f3` / `#2f3036` / `var(--surface-raised)` |
| `--lvv-color-fill-transparency-block` | `#33668014` / `var(--icon-bg)` / `#e5ecff1a` |
| `--lvv-color-fill-transparency-disable` | `var(--surface)` |
| `--lvv-color-fill-transparency-hover` | `#456c801f` / `var(--hover)` / `#e5ecff24` |
| `--lvv-color-fill-transparency-pressed` | `var(--selected)` / `#4f70802e` / `#e5ecff2e` |
| `--lvv-color-info-1` | `#e0e8ff` |
| `--lvv-color-info-2` | `#82a1ff` |
| `--lvv-color-info-3` | `#597eff` |
| `--lvv-color-info-4` | `#415fdb` |
| `--lvv-color-info-5` | `#132467` |
| `--lvv-color-info-active` | `#0b46b1` |
| `--lvv-color-info-bg` | `#2668ff33` / `rgba(38,104,255,.2)` |
| `--lvv-color-info-hover` | `#105fd4` |
| `--lvv-color-info-primary` | `#2668ff` |
| `--lvv-color-line-1` | `#07324729` / `var(--strong-line)` / `#00000029` |
| `--lvv-color-line-2` | `hsla(0,0%,100%,.28)` / `#ffffff1f` / `hsla(0,0%,100%,.12)` |
| `--lvv-color-line-3` | `#ffffff0f` / `#0732470f` / `hsla(0,0%,100%,.06)` |
| `--lvv-color-linear-1` | `linear-gradient(180deg,#0000 0%,#0003 100%)` / `linear-gradient(180deg,transparent,rgba(0,0,0,.2))` |
| `--lvv-color-linear-2` | `linear-gradient(180deg,#0000 0%,#0009 100%)` / `linear-gradient(180deg,transparent,rgba(0,0,0,.6))` |
| `--lvv-color-linear-3` | `linear-gradient(180deg,#0000 0%,#0009 100%)` / `linear-gradient(180deg,transparent,rgba(0,0,0,.6))` |
| `--lvv-color-linear-4` | `linear-gradient(180deg,#0000 0%,#0009 100%)` / `linear-gradient(180deg,transparent,rgba(0,0,0,.6))` |
| `--lvv-color-main-006` | `#00cae00f` / `rgba(0,202,224,.06)` |
| `--lvv-color-main-012` | `#00cae01f` / `rgba(0,202,224,.12)` / `hsla(0,0%,100%,.12)` |
| `--lvv-color-main-02` | `#00cae033` / `rgba(0,202,224,.2)` |
| `--lvv-color-main-04` | `#00cae066` / `rgba(0,202,224,.4)` / `#d6e4ff` |
| `--lvv-color-main-06` | `#00cae099` / `rgba(0,202,224,.6)` |
| `--lvv-color-main-08` | `#00cae0cc` / `rgba(0,202,224,.8)` |
| `--lvv-color-main-1` | `#daf5f8` |
| `--lvv-color-main-2` | `#7cdfeb` |
| `--lvv-color-main-3` | `#1fc4d9` |
| `--lvv-color-main-4` | `#19abbe` |
| `--lvv-color-main-5` | `#12525a` |
| `--lvv-color-main-alpha-1` | `#1fc4d91f` / `rgba(31,196,217,.12)` |
| `--lvv-color-main-alpha-2` | `#1fc4d933` / `rgba(31,196,217,.2)` |
| `--lvv-color-main-alpha-3` | `#1fc4d966` / `rgba(31,196,217,.4)` |
| `--lvv-color-main-alpha-4` | `#1fc4d999` / `rgba(31,196,217,.6)` |
| `--lvv-color-main-alpha-5` | `#1fc4d9cc` / `rgba(31,196,217,.8)` |
| `--lvv-color-main-default` | `#00cae0` / `#1677ff` / `var(--accent)` |
| `--lvv-color-main-hover` | `#00b1cc` / `var(--accent-hover)` / `#5084ff` |
| `--lvv-color-main-pressed` | `#0099b8` / `var(--accent-hover)` / `#245bdb` |
| `--lvv-color-negative-1` | `#ffe6e3` |
| `--lvv-color-negative-2` | `#ff9b99` |
| `--lvv-color-negative-3` | `#ff6663` |
| `--lvv-color-negative-4` | `#db4852` |
| `--lvv-color-negative-5` | `#800a12` |
| `--lvv-color-negative-active` | `#b7183e` |
| `--lvv-color-negative-bg` | `#ff666333` / `rgba(255,102,99,.2)` |
| `--lvv-color-negative-hover` | `#db233f` |
| `--lvv-color-negative-primary` | `#ff303d` |
| `--lvv-color-positive-1` | `#d5f6ea` |
| `--lvv-color-positive-2` | `#85eabc` |
| `--lvv-color-positive-3` | `#2dd196` |
| `--lvv-color-positive-4` | `#20b38d` |
| `--lvv-color-positive-5` | `#136852` |
| `--lvv-color-positive-active` | `#169681` |
| `--lvv-color-positive-bg` | `#2dd19633` / `rgba(45,209,150,.2)` |
| `--lvv-color-positive-hover` | `#20b38d` |
| `--lvv-color-positive-primary` | `#2dd196` |
| `--lvv-color-scenes-guide` | `#ffe357eb` / `rgba(255,227,87,.92)` |
| `--lvv-color-scenes-overlay` | `#fff` / `#2f3036` |
| `--lvv-color-scenes-panel` | `#ffffffe6` / `#121214cc` / `hsla(0,0%,100%,.9)` |
| `--lvv-color-scenes-toast` | `#27272f` |
| `--lvv-color-secondary-blue` | `#24a3ff` |
| `--lvv-color-secondary-blueviolet` | `#8120fd` |
| `--lvv-color-secondary-fushsia` | `#ee31ff` |
| `--lvv-color-secondary-green` | `#00c17c` |
| `--lvv-color-secondary-orange` | `#ff7a00` |
| `--lvv-color-secondary-slateblue` | `#6461ff` |
| `--lvv-color-smart-tools` | `#7153e6` |
| `--lvv-color-text-1` | `#16161d` / `#e6e6e6` / `var(--text)` |
| `--lvv-color-text-2` | `#46464c` / `#afafb6` / `var(--muted)` |
| `--lvv-color-text-3` | `#757580` / `#7a7a85` / `var(--subtle)` |
| `--lvv-color-text-4` | `#a9adb5` / `#646568` |
| `--lvv-color-text-5` | `#cacad0` / `#44444b` |
| `--lvv-color-text-content-1` | `#fff` |
| `--lvv-color-text-content-2` | `#cacace` |
| `--lvv-color-text-content-3` | `#95959d` |
| `--lvv-color-text-content-4` | `#808286` |
| `--lvv-color-text-content-5` | `#62626d` |
| `--lvv-color-text-content-disable` | `#b2d5e640` / `rgba(178,213,230,.25)` |
| `--lvv-color-text-content-placeholder` | `#b8d3e066` / `rgba(184,211,224,.4)` |
| `--lvv-color-text-content-primary` | `#fff` / `#10282b` / `#000` |
| `--lvv-color-text-content-secondary` | `#c2cfd6cc` / `rgba(194,207,214,.8)` |
| `--lvv-color-text-content-tertiary` | `#bdd1db80` / `rgba(189,209,219,.5)` |
| `--lvv-color-text-disable` | `#1b3d5f33` / `var(--subtle)` / `#dee3f733` |
| `--lvv-color-text-inverted` | `#e6e6e6` / `#16161d` / `#fafafa` |
| `--lvv-color-text-placeholder` | `#18334e66` / `var(--muted)` / `#e5e9fa66` |
| `--lvv-color-text-primary` | `#090c14` / `#fafbff` / `var(--text)` |
| `--lvv-color-text-secondary` | `#111a2cb3` / `var(--muted)` / `#f6f7ffb3` |
| `--lvv-color-text-tertiary` | `#15293c80` / `var(--muted)` / `#edf0fd80` |
| `--lvv-color-track-blue` | `#5281e6` |
| `--lvv-color-track-blueviolet` | `#7053e6` |
| `--lvv-color-track-green` | `#00ab84` |
| `--lvv-color-track-orange` | `#e67626` |
| `--lvv-color-track-pink` | `#de5088` |
| `--lvv-color-track-purple` | `#a553e6` |
| `--lvv-color-warning-1` | `#fff7e5` |
| `--lvv-color-warning-2` | `#ffd670` |
| `--lvv-color-warning-3` | `#ffaf02` |
| `--lvv-color-warning-4` | `#fb9600` |
| `--lvv-color-warning-5` | `#996900` |
| `--lvv-color-warning-active` | `#f5ae0a` |
| `--lvv-color-warning-bg` | `#ffcf3033` / `rgba(255,207,48,.2)` |
| `--lvv-color-warning-hover` | `#ffc724` |
| `--lvv-color-warning-primary` | `#ffcf30` |
| `--lvv-color-white-004` | `#ffffff0a` / `hsla(0,0%,100%,.04)` |
| `--lvv-color-white-012` | `#ffffff1f` / `hsla(0,0%,100%,.12)` |
| `--lvv-color-white-02` | `#fff3` / `hsla(0,0%,100%,.2)` |
| `--lvv-color-white-04` | `#fff6` / `hsla(0,0%,100%,.4)` |
| `--lvv-color-white-06` | `#fff9` / `hsla(0,0%,100%,.6)` |
| `--lvv-color-white-08` | `#fffc` / `hsla(0,0%,100%,.8)` |
| `--lvv-color-white-1` | `#ffffff0a` / `hsla(0,0%,100%,.04)` |
| `--lvv-color-white-2` | `#ffffff1f` / `hsla(0,0%,100%,.12)` |
| `--lvv-color-white-3` | `#fff3` / `hsla(0,0%,100%,.2)` |
| `--lvv-color-white-4` | `#fff6` / `hsla(0,0%,100%,.4)` |
| `--lvv-color-white-5` | `#fff9` / `hsla(0,0%,100%,.6)` |
| `--lvv-color-white-6` | `#fffc` / `hsla(0,0%,100%,.8)` |
| `--lvv-color-white-7` | `#fff` |
| `--lvv-color-white-inverted` | `#fff` / `#000` |
| `--lvv-color-white-stationary` | `#fff` / `#000` |
| `--lvv-color-white-tooltip` | `#f3f3f3` |
| `--lvv-line-height-body-1` | `24px` |
| `--lvv-line-height-body-2` | `20px` |
| `--lvv-line-height-caption` | `16px` |
| `--lvv-line-height-h1` | `48px` |
| `--lvv-line-height-h2` | `32px` |
| `--lvv-line-height-h3` | `24px` |
| `--lvv-line-height-title` | `56px` |
| `--lvv-shadow-008` | `#1f426614` / `#ffffff14` / `rgba(31,66,102,.08)` |
| `--lvv-shadow-016` | `#1f426629` / `#ffffff29` / `rgba(31,66,102,.16)` |
| `--lvv-shadow-024` | `#1f42663d` / `#ffffff3d` / `rgba(31,66,102,.24)` |
| `--lvv-shadow-032` | `#1f426652` / `#ffffff52` / `rgba(31,66,102,.32)` |
| `--lvv-shadow-inputfocus` | `#00c1cd33` / `rgba(0,193,205,.2)` / `transparent` |
| `--lvv-size-body-1` | `16px` |
| `--lvv-size-body-2` | `14px` |
| `--lvv-size-caption` | `12px` |
| `--lvv-size-h1` | `32px` |
| `--lvv-size-h2` | `24px` |
| `--lvv-size-h3` | `18px` |
| `--lvv-size-title` | `36px` |
| `--magenta-1` | `255,232,241` / `77,0,52` |
| `--magenta-10` | `77,0,52` / `255,232,241` |
| `--magenta-2` | `253,194,219` / `119,8,80` |
| `--magenta-3` | `251,157,199` / `161,23,108` |
| `--magenta-4` | `249,121,183` / `203,43,136` |
| `--magenta-5` | `247,84,168` / `245,69,166` |
| `--magenta-6` | `245,49,157` / `247,86,169` |
| `--magenta-7` | `203,30,131` / `249,122,184` |
| `--magenta-8` | `161,16,105` / `251,158,200` |
| `--magenta-9` | `119,6,79` / `253,195,219` |
| `--manage-button-icon` | `url(images/toolbarButton-pageDown.svg)` |
| `--media-card-object-fit` | `cover` |
| `--media-preview-dialog-height` | `-moz-calc(100vh - 96px)` / `calc(100vh - 96px)` / `-moz-calc(100vh - 40px)` |
| `--mention-menu-gap` | `6px` |
| `--mention-menu-viewport-margin` | `8px` |
| `--menu-backdrop-filter` | `none` |
| `--menu-background-blend-mode` | `normal` |
| `--menu-bg` | `var(--background-color-box, light-dark(white, #23222b))` / `var(--background-color-box, Canvas)` |
| `--menu-border-color` | `light-dark(rgb(21 20 26 / 0.1), rgb(251 251 254 / 0.1))` / `CanvasText` |
| `--menu-box-shadow` | `0 0.375px 1.5px 0 light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / ` / `none` |
| `--menu-icon-size` | `16px` |
| `--menu-mark-icon-size` | `0` / `16px` |
| `--menu-text-color` | `var(--text-color, light-dark(#15141a, #fbfbfe))` / `var(--text-color, ButtonText)` |
| `--menu-text-disabled-color` | `var(--menu-text-color)` / `GrayText` |
| `--menuitem-active-bg` | `color-mix(
    in srgb,
    var(--menu-text-color),
    tran` / `SelectedItemText` |
| `--menuitem-active-border-color` | `var(--menuitem-border-color)` / `ButtonText` |
| `--menuitem-attachmentsView-icon` | `url(images/toolbarButton-viewAttachments.svg)` |
| `--menuitem-border-color` | `transparent` / `none` |
| `--menuitem-border-radius` | `8px` |
| `--menuitem-checkmark-icon` | `url(images/checkmark.svg)` |
| `--menuitem-focus-bg` | `color-mix(
    in srgb,
    var(--menu-text-color),
    tran` / `ButtonFace` |
| `--menuitem-focus-border-color` | `light-dark(white, black)` / `none` |
| `--menuitem-focus-outline-color` | `var(
    --focus-outline-color,
    light-dark(#0062fa, #00c` / `var(--focus-outline-color, CanvasText)` |
| `--menuitem-gap` | `5px` |
| `--menuitem-hover-background-blend-mode` | `normal` |
| `--menuitem-hover-bg` | `color-mix(
    in srgb,
    var(--menu-text-color),
    tran` / `SelectedItemText` |
| `--menuitem-layersView-icon` | `url(images/toolbarButton-viewLayers.svg)` |
| `--menuitem-outlinesView-icon` | `url(images/toolbarButton-viewOutline.svg)` |
| `--menuitem-text-active-fg` | `var(--menu-text-color)` / `SelectedItem` |
| `--menuitem-text-hover-fg` | `var(--menu-text-color)` / `SelectedItem` |
| `--menuitem-thumbnailsView-icon` | `url(images/pages_viewButton.svg)` |
| `--message-bar-bg-color` | `light-dark(#deeafc, #003070)` / `Canvas` / `light-dark(#ffebcd, #5a3100)` |
| `--message-bar-border-color` | `CanvasText` / `light-dark(
    rgb(0 0 0 / 0.08),
    rgb(255 255 255 / 0.0` / `light-dark(
        rgb(0 0 0 / 0.08),
        rgb(255 255 2` |
| `--message-bar-close-button-active-bg-color` | `var(
    --button-background-color-active,
    light-dark(rg` / `var(
      --button-background-color-hover,
      SelectedIt` |
| `--message-bar-close-button-border` | `none` / `1px solid var(--button-border-color, ButtonText)` |
| `--message-bar-close-button-border-radius` | `var(--border-radius-small, 4px)` |
| `--message-bar-close-button-color` | `var(--text-primary-color)` / `var(--button-text-color, ButtonText)` |
| `--message-bar-close-button-color-hover` | `var(--text-primary-color)` / `var(
      --button-text-color-hover,
      SelectedItem
   ` |
| `--message-bar-close-button-focus-bg-color` | `var(
    --button-background-color,
    light-dark(rgb(21 20` / `var(
      --button-background-color-hover,
      SelectedIt` |
| `--message-bar-close-button-hover-bg-color` | `var(
    --button-background-color-hover,
    light-dark(rgb` / `var(
      --button-background-color-hover,
      SelectedIt` |
| `--message-bar-fg-color` | `var(--text-primary-color)` / `light-dark(#15141a, #fbfbfe)` / `CanvasText` |
| `--message-bar-icon` | `url(images/messageBar_info.svg)` / `url(images/messageBar_warning.svg)` |
| `--message-bar-icon-color` | `CanvasText` / `light-dark(#0060df, #73a7f3)` / `light-dark(#cd411e, #e49c49)` |
| `--min-font-size` | `1` |
| `--min-font-size-inv` | `calc(1 / var(--min-font-size))` |
| `--mode-QOjY8A` | `hover .lv-select-view{background-color:hsla(0,0%,100%,.08)!i` |
| `--model-yRARsV` | `:-webkit-scrollbar{background:transparent` / `:-webkit-scrollbar-corner{background:transparent` / `:-webkit-scrollbar-track{background-color:transparent` |
| `--multiple-dragging-bg` | `white` / `Canvas` |
| `--multiple-dragging-indicator-bg` | `var(--indicator-color)` / `var(--text-color, ButtonBorder)` |
| `--multiple-dragging-text-color` | `light-dark(#fbfbfe, #15141a)` / `Canvas` |
| `--muted` | `var(--skill-muted,#adb2b9)` |
| `--new-alt-text-ai-disclaimer-icon` | `url(images/altText_disclaimer.svg)` |
| `--new-alt-text-spinner-icon` | `url(images/altText_spinner.svg)` |
| `--new-alt-text-warning-image` | `url(images/altText_warning.svg)` |
| `--new-badge-bg` | `light-dark(#070, #37b847)` / `AccentColor` |
| `--new-badge-border-color` | `light-dark(#fbfbfe / 40%, #15141a / 40%)` / `CanvasText` |
| `--new-badge-color` | `light-dark(#fff, #15141a)` / `ButtonFace` |
| `--no-alt-text-badge-bg-color` | `light-dark(#cfcfd8, #fbfbfe)` / `ButtonFace` |
| `--no-alt-text-badge-border-color` | `light-dark(#f0f0f4, #52525e)` / `ButtonText` |
| `--no-alt-text-badge-fg-color` | `light-dark(#5b5b66, #15141a)` / `ButtonText` |
| `--node-card-border-color` | `transparent` / `hsla(0,0%,100%,.06)` / `hsla(0,0%,100%,.2)` |
| `--node-card-outline-color` | `transparent` / `hsla(0,0%,100%,.5)` / `hsla(0,0%,100%,.2)` |
| `--node-card-overlay-outline-color` | `transparent` / `transparent!important` / `hsla(0,0%,100%,.2)` |
| `--node-resize-container-border-width` | `0px` |
| `--node-selection-flow-top` | `24px` / `0px` |
| `--node-selection-outline-color` | `hsla(0,0%,100%,.5)` / `transparent` / `hsla(0,0%,100%,.2)` |
| `--node-surface-border-color` | `hsla(0,0%,100%,.06)` / `hsla(0,0%,100%,.25)` / `hsla(0,0%,100%,.75)` |
| `--open-link-fg` | `var(--link-fg-color)` / `ButtonText` |
| `--open-link-hover-fg` | `var(--link-hover-fg-color)` / `ButtonText` |
| `--orange-1` | `255,247,232` / `77,27,0` |
| `--orange-10` | `77,27,0` / `255,247,232` |
| `--orange-2` | `255,228,186` / `121,48,4` |
| `--orange-3` | `255,207,139` / `166,75,10` |
| `--orange-4` | `255,182,93` / `210,105,19` |
| `--orange-5` | `255,154,46` / `255,141,31` |
| `--orange-6` | `255,125,0` / `255,150,38` |
| `--orange-7` | `210,95,0` / `255,179,87` |
| `--orange-8` | `166,69,0` / `255,205,135` |
| `--orange-9` | `121,46,0` / `255,227,184` |
| `--orangered-1` | `255,243,232` / `77,14,0` |
| `--orangered-10` | `77,14,0` / `255,244,235` |
| `--orangered-2` | `253,221,195` / `119,30,5` |
| `--orangered-3` | `252,197,159` / `162,55,20` |
| `--orangered-4` | `250,172,123` / `204,87,41` |
| `--orangered-5` | `249,144,87` / `247,126,69` |
| `--orangered-6` | `247,114,52` / `249,146,90` |
| `--orangered-7` | `204,81,32` / `250,173,125` |
| `--orangered-8` | `162,53,17` / `252,198,161` |
| `--orangered-9` | `119,31,6` / `253,222,197` |
| `--outline-around-color` | `var(--color-gray-20, #f0f0f4)` / `ButtonFace` |
| `--outline-around-width` | `1px` |
| `--outline-color` | `var(--color-blue-60, #0060df)` / `CanvasText` |
| `--outline-width` | `2px` |
| `--overlay-bg` | `var(--skill-overlay-bg,#0009)` |
| `--page-bg` | `var(--skill-page-bg,#1c1c1c)` |
| `--page-bg-color` | `unset` |
| `--page-border` | `9px solid transparent` / `1px solid CanvasText` |
| `--page-margin` | `1px auto -8px` / `8px auto -1px` |
| `--pages-selected-icon` | `url(images/pages_selected.svg)` |
| `--panel-bg` | `var(--skill-panel-bg,#222528)` |
| `--pdfViewer-padding-bottom` | `0` / `9px` |
| `--permission-full-color` | `#ff9a62` / `#ab3f00` |
| `--permission-selected-bg` | `#3c4044` / `#edf1f4` |
| `--phase-background` | `var(--selected)` / `var(--surface)` |
| `--phase-color` | `var(--text)` / `var(--warning)` |
| `--pinkpurple-1` | `255,232,251` / `66,0,77` |
| `--pinkpurple-10` | `66,0,77` / `255,242,253` |
| `--pinkpurple-2` | `247,186,239` / `101,3,112` |
| `--pinkpurple-3` | `240,142,230` / `138,13,147` |
| `--pinkpurple-4` | `232,101,223` / `176,27,182` |
| `--pinkpurple-5` | `225,62,219` / `217,46,217` |
| `--pinkpurple-6` | `217,26,217` / `225,61,219` |
| `--pinkpurple-7` | `176,16,182` / `232,102,223` |
| `--pinkpurple-8` | `138,9,147` / `240,146,230` |
| `--pinkpurple-9` | `101,3,112` / `247,193,240` |
| `--popup-bg` | `var(--skill-popup-bg,#32363a)` |
| `--preview-image-bg-color` | `light-dark(#f0f0f4, #2b2a33)` / `ButtonFace` |
| `--preview-image-border` | `none` / `1px solid ButtonText` |
| `--primary-1` | `var(--arcoblue-1)` |
| `--primary-10` | `var(--arcoblue-10)` |
| `--primary-2` | `var(--arcoblue-2)` |
| `--primary-3` | `var(--arcoblue-3)` |
| `--primary-4` | `var(--arcoblue-4)` |
| `--primary-5` | `var(--arcoblue-5)` |
| `--primary-6` | `var(--arcoblue-6)` |
| `--primary-7` | `var(--arcoblue-7)` |
| `--primary-8` | `var(--arcoblue-8)` |
| `--primary-9` | `var(--arcoblue-9)` |
| `--primary-color` | `var(--text-primary-color)` / `ButtonText` |
| `--prompt-fade-bottom` | `0px` / `12px` |
| `--prompt-fade-top` | `0px` / `12px` |
| `--purple-1` | `245,232,255` / `22,0,77` |
| `--purple-10` | `22,0,77` / `247,237,255` |
| `--purple-2` | `221,190,246` / `39,6,110` |
| `--purple-3` | `195,150,237` / `62,19,143` |
| `--purple-4` | `168,113,227` / `90,37,176` |
| `--purple-5` | `141,78,218` / `123,61,209` |
| `--purple-6` | `114,46,209` / `142,81,218` |
| `--purple-7` | `85,29,176` / `169,116,227` |
| `--purple-8` | `60,16,143` / `197,154,237` |
| `--purple-9` | `39,6,110` / `223,194,246` |
| `--radius-content` | `12px` |
| `--radius-control` | `8px` |
| `--radius-dialog` | `20px` |
| `--radius-panel` | `16px` |
| `--radius-pill` | `999px` |
| `--red-0` | `#450b0b` |
| `--red-1` | `#ae1c1c` / `255,236,232` / `77,0,10` |
| `--red-10` | `77,0,10` / `255,240,236` |
| `--red-2` | `253,205,197` / `119,6,17` |
| `--red-3` | `251,172,163` / `161,22,31` |
| `--red-4` | `249,137,129` / `203,46,52` |
| `--red-5` | `247,101,96` / `245,78,78` |
| `--red-6` | `245,63,63` / `247,105,101` |
| `--red-7` | `203,39,45` / `249,141,134` |
| `--red-8` | `161,21,30` / `251,176,167` |
| `--red-9` | `119,8,19` / `253,209,202` |
| `--reference-action-tCDg2s` | `:-webkit-scrollbar{background:transparent` / `:-webkit-scrollbar-corner{background:transparent` / `:-webkit-scrollbar-track{background-color:transparent` |
| `--resize-arc-scale` | `-moz-calc(var(--canvas-node-radius-scale,1)*12/15.5 + var(--` / `calc(var(--canvas-node-radius-scale, 1)*12/15.5 + var(--canv` |
| `--resize-icon-offset` | `-moz-calc(0.5px*var(--canvas-node-outline-scale,1) - 1.5px*v` / `calc(0.5px*var(--canvas-node-outline-scale, 1) - 1.5px*var(-` |
| `--resizer-bg-color` | `var(--outline-color)` / `ButtonText` |
| `--resizer-hover-bg-color` | `var(
    --color-accent-primary,
    light-dark(#0062fa, #00` / `var(--text-color, CanvasText)` |
| `--resizer-shift` | `calc(
    0px - (var(--outline-width) + var(--resizer-size))` / `calc(0px - var(--resizer-width) - 2px)` |
| `--resizer-size` | `6px` |
| `--resizer-width` | `4px` |
| `--result-stack-backdrop-offset` | `44px` |
| `--result-stack-grid-gap` | `8px` |
| `--rotate` | `0deg` |
| `--save-warning-color` | `var(--secondary-color)` |
| `--scale-factor` | `1` |
| `--scale-round-x` | `1px` |
| `--scale-round-y` | `1px` |
| `--scale-x` | `1` |
| `--script-editor-dialog-height` | `-moz-calc(100vh - 96px)` / `calc(100vh - 96px)` / `-moz-calc(100vh - 32px)` |
| `--script-table-columns` | `64px 64px repeat(4,minmax(200px,1fr))` |
| `--scrollbar` | `var(--skill-scrollbar,#ffffff26)` |
| `--search-active-bg` | `var(--skill-search-active-bg,#a36a27)` |
| `--search-bg` | `var(--skill-search-bg,#6d582d)` |
| `--secondary-color` | `var(--text-secondary-color)` / `ButtonText` |
| `--selected` | `var(--skill-selected,#ffffff1f)` |
| `--selected-outline-color` | `light-dark(#0060df, #aaf2ff)` / `var(--hover-outline-color)` |
| `--semi-amber-0` | `254,251,235` / `81,46,9` |
| `--semi-amber-1` | `252,245,206` / `121,75,15` |
| `--semi-amber-2` | `249,232,158` / `161,107,22` |
| `--semi-amber-3` | `246,216,111` / `202,143,30` |
| `--semi-amber-4` | `243,198,65` / `242,183,38` |
| `--semi-amber-5` | `240,177,20` / `245,202,80` |
| `--semi-amber-6` | `200,138,15` / `247,219,122` |
| `--semi-amber-7` | `160,102,10` / `250,234,166` |
| `--semi-amber-8` | `120,70,6` / `252,246,210` |
| `--semi-amber-9` | `80,43,3` / `254,251,237` |
| `--semi-black` | `0,0,0` |
| `--semi-blue-0` | `234,245,255` / `5,49,112` |
| `--semi-blue-1` | `203,231,254` / `10,70,148` |
| `--semi-blue-2` | `152,205,253` / `19,92,184` |
| `--semi-blue-3` | `101,178,252` / `29,117,219` |
| `--semi-blue-4` | `50,149,251` / `41,144,255` |
| `--semi-blue-5` | `0,100,250` / `84,169,255` |
| `--semi-blue-6` | `0,98,214` / `127,193,255` |
| `--semi-blue-7` | `0,79,179` / `169,215,255` |
| `--semi-blue-8` | `0,61,143` / `212,236,255` |
| `--semi-blue-9` | `0,44,107` / `239,248,255` |
| `--semi-border-radius-circle` | `50%` |
| `--semi-border-radius-extra-small` | `4px` / `3px` |
| `--semi-border-radius-full` | `9999px` |
| `--semi-border-radius-large` | `12px` |
| `--semi-border-radius-medium` | `6px` |
| `--semi-border-radius-small` | `1px` / `3px` |
| `--semi-color-bg-0` | `rgba(var(--semi-white),1)` / `#16161a` |
| `--semi-color-bg-1` | `rgba(var(--semi-white),1)` / `#232429` |
| `--semi-color-bg-2` | `rgba(var(--semi-white),1)` / `#35363c` |
| `--semi-color-bg-3` | `var(--black-0)` / `rgba(var(--semi-white),1)` / `#43444a` |
| `--semi-color-bg-4` | `rgba(var(--semi-white),1)` / `#4f5159` |
| `--semi-color-black` | `rgba(var(--semi-black),1)` |
| `--semi-color-border` | `rgba(var(--semi-grey-9),.08)` / `rgba(var(--semi-white),.08)` |
| `--semi-color-danger` | `var(--red-1)` / `rgba(var(--semi-red-5),1)` |
| `--semi-color-danger-active` | `rgba(var(--semi-red-7),1)` |
| `--semi-color-danger-hover` | `rgba(var(--semi-red-6),1)` |
| `--semi-color-danger-light-active` | `rgba(var(--semi-red-2),1)` / `rgba(var(--semi-red-5),.4)` |
| `--semi-color-danger-light-default` | `rgba(var(--semi-red-0),1)` / `rgba(var(--semi-red-5),.2)` |
| `--semi-color-danger-light-hover` | `rgba(var(--semi-red-1),1)` / `rgba(var(--semi-red-5),.3)` |
| `--semi-color-data-0` | `#1664ff` |
| `--semi-color-data-1` | `#b2cfff` |
| `--semi-color-data-10` | `#ffc400` |
| `--semi-color-data-11` | `#fae878` |
| `--semi-color-data-12` | `#304d77` |
| `--semi-color-data-13` | `#8b959e` |
| `--semi-color-data-14` | `#b48deb` |
| `--semi-color-data-15` | `#efe3ff` |
| `--semi-color-data-16` | `#009488` |
| `--semi-color-data-17` | `#59baa8` |
| `--semi-color-data-18` | `#ff7dda` |
| `--semi-color-data-19` | `#ffcfee` |
| `--semi-color-data-2` | `#1ac6ff` |
| `--semi-color-data-3` | `#94efff` |
| `--semi-color-data-4` | `#ff8a00` |
| `--semi-color-data-5` | `#ffce7a` |
| `--semi-color-data-6` | `#3cc780` |
| `--semi-color-data-7` | `#b9edcd` |
| `--semi-color-data-8` | `#7442d4` |
| `--semi-color-data-9` | `#ddc5fa` |
| `--semi-color-default` | `rgba(var(--semi-grey-0),1)` |
| `--semi-color-default-active` | `rgba(var(--semi-grey-2),1)` |
| `--semi-color-default-hover` | `rgba(var(--semi-grey-1),1)` |
| `--semi-color-disabled-bg` | `rgba(var(--semi-grey-1),1)` |
| `--semi-color-disabled-border` | `rgba(var(--semi-grey-1),1)` |
| `--semi-color-disabled-fill` | `rgba(var(--semi-grey-8),.04)` |
| `--semi-color-disabled-text` | `var(--black-5)` / `var(--indigo-0)` / `rgba(var(--semi-grey-9),.35)` |
| `--semi-color-fill-0` | `rgba(var(--semi-grey-8),.05)` / `rgba(var(--semi-white),.12)` |
| `--semi-color-fill-1` | `rgba(var(--semi-grey-8),.09)` / `rgba(var(--semi-white),.16)` |
| `--semi-color-fill-2` | `rgba(var(--semi-grey-8),.13)` / `rgba(var(--semi-white),.20)` |
| `--semi-color-focus-border` | `var(--cyan-2)` / `rgba(var(--semi-blue-5),1)` |
| `--semi-color-highlight` | `rgba(var(--semi-black),1)` / `rgba(var(--semi-white),1)` |
| `--semi-color-highlight-bg` | `rgba(var(--semi-yellow-4),1)` / `rgba(var(--semi-yellow-2),1)` |
| `--semi-color-info` | `rgba(var(--semi-blue-5),1)` |
| `--semi-color-info-active` | `rgba(var(--semi-blue-7),1)` |
| `--semi-color-info-disabled` | `rgba(var(--semi-blue-2),1)` |
| `--semi-color-info-hover` | `rgba(var(--semi-blue-6),1)` |
| `--semi-color-info-light-active` | `rgba(var(--semi-blue-2),1)` / `rgba(var(--semi-blue-5),.4)` |
| `--semi-color-info-light-default` | `rgba(var(--semi-blue-0),1)` / `rgba(var(--semi-blue-5),.2)` |
| `--semi-color-info-light-hover` | `rgba(var(--semi-blue-1),1)` / `rgba(var(--semi-blue-5),.3)` |
| `--semi-color-link` | `rgba(var(--semi-blue-5),1)` |
| `--semi-color-link-active` | `rgba(var(--semi-blue-7),1)` |
| `--semi-color-link-hover` | `rgba(var(--semi-blue-6),1)` |
| `--semi-color-link-visited` | `rgba(var(--semi-blue-5),1)` |
| `--semi-color-nav-bg` | `rgba(var(--semi-white),1)` / `#232429` |
| `--semi-color-overlay-bg` | `var(--alpha-60b)` / `#16161a99` |
| `--semi-color-primary` | `var(--cyan-2)` / `rgba(var(--semi-blue-5),1)` |
| `--semi-color-primary-active` | `var(--cyan-1)` / `rgba(var(--semi-blue-7),1)` |
| `--semi-color-primary-disabled` | `var(--cyan-0)` / `rgba(var(--semi-blue-2),1)` |
| `--semi-color-primary-hover` | `var(--cyan-3)` / `rgba(var(--semi-blue-6),1)` |
| `--semi-color-primary-light-active` | `rgba(var(--semi-blue-2),1)` / `rgba(var(--semi-blue-5),.4)` |
| `--semi-color-primary-light-default` | `rgba(var(--semi-blue-0),1)` / `rgba(var(--semi-blue-5),.2)` |
| `--semi-color-primary-light-hover` | `rgba(var(--semi-blue-1),1)` / `rgba(var(--semi-blue-5),.3)` |
| `--semi-color-secondary` | `var(--indigo-0)` / `rgba(var(--semi-light-blue-5),1)` |
| `--semi-color-secondary-active` | `var(--black-2)` / `rgba(var(--semi-light-blue-7),1)` |
| `--semi-color-secondary-disabled` | `var(--black-4)` / `rgba(var(--semi-light-blue-2),1)` |
| `--semi-color-secondary-hover` | `var(--indigo-2)` / `rgba(var(--semi-light-blue-6),1)` |
| `--semi-color-secondary-light-active` | `rgba(var(--semi-light-blue-2),1)` / `rgba(var(--semi-light-blue-5),.4)` |
| `--semi-color-secondary-light-default` | `rgba(var(--semi-light-blue-0),1)` / `rgba(var(--semi-light-blue-5),.2)` |
| `--semi-color-secondary-light-hover` | `rgba(var(--semi-light-blue-1),1)` / `rgba(var(--semi-light-blue-5),.3)` |
| `--semi-color-shadow` | `rgba(var(--semi-black),.04)` |
| `--semi-color-success` | `rgba(var(--semi-green-5),1)` |
| `--semi-color-success-active` | `rgba(var(--semi-green-7),1)` |
| `--semi-color-success-disabled` | `rgba(var(--semi-green-2),1)` |
| `--semi-color-success-hover` | `rgba(var(--semi-green-6),1)` |
| `--semi-color-success-light-active` | `rgba(var(--semi-green-2),1)` / `rgba(var(--semi-green-5),.4)` |
| `--semi-color-success-light-default` | `rgba(var(--semi-green-0),1)` / `rgba(var(--semi-green-5),.2)` |
| `--semi-color-success-light-hover` | `rgba(var(--semi-green-1),1)` / `rgba(var(--semi-green-5),.3)` |
| `--semi-color-tertiary` | `rgba(var(--semi-grey-5),1)` |
| `--semi-color-tertiary-active` | `rgba(var(--semi-grey-7),1)` |
| `--semi-color-tertiary-hover` | `rgba(var(--semi-grey-6),1)` |
| `--semi-color-tertiary-light-active` | `rgba(var(--semi-grey-2),1)` / `rgba(var(--semi-grey-5),.4)` |
| `--semi-color-tertiary-light-default` | `rgba(var(--semi-grey-0),1)` / `rgba(var(--semi-grey-5),.2)` |
| `--semi-color-tertiary-light-hover` | `rgba(var(--semi-grey-1),1)` / `rgba(var(--semi-grey-5),.3)` |
| `--semi-color-text-0` | `rgba(var(--semi-grey-9),1)` |
| `--semi-color-text-1` | `rgba(var(--semi-grey-9),.8)` |
| `--semi-color-text-2` | `rgba(var(--semi-grey-9),.62)` / `rgba(var(--semi-grey-9),.6)` |
| `--semi-color-text-3` | `rgba(var(--semi-grey-9),.35)` |
| `--semi-color-warning` | `rgba(var(--semi-orange-5),1)` |
| `--semi-color-warning-active` | `rgba(var(--semi-orange-7),1)` |
| `--semi-color-warning-hover` | `rgba(var(--semi-orange-6),1)` |
| `--semi-color-warning-light-active` | `rgba(var(--semi-orange-2),1)` / `rgba(var(--semi-orange-5),.4)` |
| `--semi-color-warning-light-default` | `rgba(var(--semi-orange-0),1)` / `rgba(var(--semi-orange-5),.2)` |
| `--semi-color-warning-light-hover` | `rgba(var(--semi-orange-1),1)` / `rgba(var(--semi-orange-5),.3)` |
| `--semi-color-white` | `rgba(var(--semi-white),1)` / `#e4e7f5` |
| `--semi-cyan-0` | `229,247,248` / `4,52,61` |
| `--semi-cyan-1` | `194,239,240` / `7,79,92` |
| `--semi-cyan-2` | `138,221,226` / `10,108,123` |
| `--semi-cyan-3` | `88,203,211` / `14,137,153` |
| `--semi-cyan-4` | `44,184,197` / `19,168,184` |
| `--semi-cyan-5` | `5,164,182` / `56,187,198` |
| `--semi-cyan-6` | `3,134,152` / `98,205,212` |
| `--semi-cyan-7` | `1,105,121` / `145,223,227` |
| `--semi-cyan-8` | `0,77,91` / `198,239,241` |
| `--semi-cyan-9` | `0,50,61` / `231,247,248` |
| `--semi-green-0` | `236,247,236` / `18,60,25` |
| `--semi-green-1` | `208,240,209` / `28,90,37` |
| `--semi-green-2` | `164,224,167` / `39,119,49` |
| `--semi-green-3` | `125,209,130` / `50,149,61` |
| `--semi-green-4` | `90,194,98` / `62,179,73` |
| `--semi-green-5` | `59,179,70` / `93,194,100` |
| `--semi-green-6` | `48,149,59` / `127,209,132` |
| `--semi-green-7` | `37,119,47` / `166,225,168` |
| `--semi-green-8` | `27,89,36` / `208,240,209` |
| `--semi-green-9` | `17,60,24` / `236,247,236` |
| `--semi-grey-0` | `249,249,249` / `28,31,35` |
| `--semi-grey-1` | `230,232,234` / `46,50,56` |
| `--semi-grey-2` | `198,202,205` / `65,70,76` |
| `--semi-grey-3` | `167,171,176` / `85,91,97` |
| `--semi-grey-4` | `136,141,146` / `107,112,117` |
| `--semi-grey-5` | `107,112,117` / `136,141,146` |
| `--semi-grey-6` | `85,91,97` / `167,171,176` |
| `--semi-grey-7` | `65,70,76` / `198,202,205` |
| `--semi-grey-8` | `46,50,56` / `230,232,234` |
| `--semi-grey-9` | `28,31,35` / `249,249,249` |
| `--semi-indigo-0` | `236,239,248` / `23,30,101` |
| `--semi-indigo-1` | `209,216,240` / `32,41,122` |
| `--semi-indigo-2` | `167,179,225` / `41,54,142` |
| `--semi-indigo-3` | `128,144,211` / `52,68,163` |
| `--semi-indigo-4` | `94,111,196` / `64,83,183` |
| `--semi-indigo-5` | `63,81,181` / `95,113,197` |
| `--semi-indigo-6` | `51,66,161` / `129,145,212` |
| `--semi-indigo-7` | `40,52,140` / `167,180,226` |
| `--semi-indigo-8` | `31,40,120` / `209,216,241` |
| `--semi-indigo-9` | `23,29,99` / `237,239,248` |
| `--semi-light-blue-0` | `233,247,253` / `0,55,97` |
| `--semi-light-blue-1` | `201,236,252` / `0,77,133` |
| `--semi-light-blue-2` | `149,216,248` / `3,102,169` |
| `--semi-light-blue-3` | `98,195,245` / `10,129,204` |
| `--semi-light-blue-4` | `48,172,241` / `19,159,240` |
| `--semi-light-blue-5` | `0,149,238` / `64,180,243` |
| `--semi-light-blue-6` | `0,123,202` / `110,200,246` |
| `--semi-light-blue-7` | `0,99,167` / `157,220,249` |
| `--semi-light-blue-8` | `0,75,131` / `206,238,252` |
| `--semi-light-blue-9` | `0,53,95` / `235,248,254` |
| `--semi-light-green-0` | `243,248,236` / `38,61,19` |
| `--semi-light-green-1` | `227,240,208` / `59,92,29` |
| `--semi-light-green-2` | `200,226,165` / `81,123,40` |
| `--semi-light-green-3` | `173,211,126` / `103,153,52` |
| `--semi-light-green-4` | `147,197,91` / `127,184,64` |
| `--semi-light-green-5` | `123,182,60` / `151,198,95` |
| `--semi-light-green-6` | `100,152,48` / `176,212,129` |
| `--semi-light-green-7` | `78,121,38` / `201,227,167` |
| `--semi-light-green-8` | `57,91,27` / `228,241,209` |
| `--semi-light-green-9` | `37,61,18` / `243,248,237` |
| `--semi-lime-0` | `242,250,230` / `49,70,3` |
| `--semi-lime-1` | `227,246,197` / `75,105,5` |
| `--semi-lime-2` | `203,237,142` / `103,141,9` |
| `--semi-lime-3` | `183,227,91` / `132,176,12` |
| `--semi-lime-4` | `167,218,44` / `162,211,17` |
| `--semi-lime-5` | `155,209,0` / `174,220,58` |
| `--semi-lime-6` | `126,174,0` / `189,229,102` |
| `--semi-lime-7` | `99,139,0` / `207,237,150` |
| `--semi-lime-8` | `72,104,0` / `229,246,201` |
| `--semi-lime-9` | `47,70,0` / `243,251,233` |
| `--semi-orange-0` | `255,248,234` / `85,31,3` |
| `--semi-orange-1` | `254,238,204` / `128,53,6` |
| `--semi-orange-2` | `254,217,152` / `170,80,10` |
| `--semi-orange-3` | `253,193,101` / `213,111,15` |
| `--semi-orange-4` | `253,166,51` / `255,146,20` |
| `--semi-orange-5` | `252,136,0` / `255,174,67` |
| `--semi-orange-6` | `210,103,0` / `255,199,114` |
| `--semi-orange-7` | `168,74,0` / `255,221,161` |
| `--semi-orange-8` | `126,49,0` / `255,239,208` |
| `--semi-orange-9` | `84,29,0` / `255,249,237` |
| `--semi-pink-0` | `253,236,239` / `92,7,48` |
| `--semi-pink-1` | `251,207,216` / `128,14,65` |
| `--semi-pink-2` | `246,160,181` / `164,23,81` |
| `--semi-pink-3` | `242,115,150` / `199,34,97` |
| `--semi-pink-4` | `237,72,123` / `235,47,113` |
| `--semi-pink-5` | `233,30,99` / `239,86,134` |
| `--semi-pink-6` | `197,19,86` / `243,126,159` |
| `--semi-pink-7` | `162,11,72` / `247,168,188` |
| `--semi-pink-8` | `126,5,58` / `251,211,220` |
| `--semi-pink-9` | `90,1,43` / `253,238,241` |
| `--semi-purple-0` | `247,233,247` / `74,16,97` |
| `--semi-purple-1` | `239,202,240` / `94,23,118` |
| `--semi-purple-2` | `221,155,224` / `115,31,138` |
| `--semi-purple-3` | `201,111,209` / `137,40,159` |
| `--semi-purple-4` | `180,73,194` / `160,51,179` |
| `--semi-purple-5` | `158,40,179` / `181,83,194` |
| `--semi-purple-6` | `135,30,158` / `202,120,209` |
| `--semi-purple-7` | `113,22,138` / `221,160,225` |
| `--semi-purple-8` | `92,15,117` / `239,206,240` |
| `--semi-purple-9` | `73,10,97` / `247,235,247` |
| `--semi-red-0` | `254,242,237` / `108,9,11` |
| `--semi-red-1` | `254,221,210` / `144,17,16` |
| `--semi-red-2` | `253,183,165` / `180,32,25` |
| `--semi-red-3` | `251,144,120` / `215,51,36` |
| `--semi-red-4` | `250,102,76` / `251,73,50` |
| `--semi-red-5` | `249,57,32` / `252,114,90` |
| `--semi-red-6` | `213,37,21` / `253,153,131` |
| `--semi-red-7` | `178,20,12` / `253,190,172` |
| `--semi-red-8` | `142,8,5` / `254,224,213` |
| `--semi-red-9` | `106,1,3` / `255,243,239` |
| `--semi-shadow-elevated` | `0 0 1px #0000004d,0 4px 14px #0000001a` / `inset 0 0 0 1px #ffffff1a,0 4px 14px #00000040` |
| `--semi-teal-0` | `228,247,244` / `2,60,57` |
| `--semi-teal-1` | `192,240,232` / `4,90,85` |
| `--semi-teal-2` | `135,224,211` / `7,119,111` |
| `--semi-teal-3` | `84,209,193` / `10,149,136` |
| `--semi-teal-4` | `39,194,176` / `14,179,161` |
| `--semi-teal-5` | `0,179,161` / `51,194,176` |
| `--semi-teal-6` | `0,149,137` / `94,209,193` |
| `--semi-teal-7` | `0,119,111` / `142,225,211` |
| `--semi-teal-8` | `0,89,85` / `196,240,232` |
| `--semi-teal-9` | `0,60,58` / `230,247,244` |
| `--semi-transform-rotate-none` | `rotate(0deg)` |
| `--semi-transform_rotate-anticlockwise180deg` | `rotate(-180deg)` |
| `--semi-transform_rotate-anticlockwise270deg` | `rotate(-270deg)` |
| `--semi-transform_rotate-anticlockwise360deg` | `rotate(-360deg)` |
| `--semi-transform_rotate-anticlockwise90deg` | `rotate(-90deg)` |
| `--semi-transform_rotate-clockwise180deg` | `rotate(180deg)` |
| `--semi-transform_rotate-clockwise270deg` | `rotate(270deg)` |
| `--semi-transform_rotate-clockwise360deg` | `rotate(360deg)` |
| `--semi-transform_rotate-clockwise90deg` | `rotate(90deg)` |
| `--semi-transform_scale-large` | `scale(1,1)` |
| `--semi-transform_scale-medium` | `scale(1,1)` |
| `--semi-transform_scale-none` | `scale(1,1)` |
| `--semi-transform_scale-small` | `scale(1,1)` |
| `--semi-transition_delay-fast` | `0ms` |
| `--semi-transition_delay-faster` | `0ms` |
| `--semi-transition_delay-fastest` | `0ms` |
| `--semi-transition_delay-none` | `0ms` |
| `--semi-transition_delay-normal` | `0ms` |
| `--semi-transition_delay-slow` | `0ms` |
| `--semi-transition_delay-slower` | `0ms` |
| `--semi-transition_delay-slowest` | `0ms` |
| `--semi-transition_duration-fast` | `0ms` |
| `--semi-transition_duration-faster` | `0ms` |
| `--semi-transition_duration-fastest` | `0ms` |
| `--semi-transition_duration-none` | `0ms` |
| `--semi-transition_duration-normal` | `0ms` |
| `--semi-transition_duration-slow` | `0ms` |
| `--semi-transition_duration-slower` | `0ms` |
| `--semi-transition_duration-slowest` | `0ms` |
| `--semi-transition_function-ease` | `ease` |
| `--semi-transition_function-easeIn` | `ease-in` |
| `--semi-transition_function-easeInIOut` | `ease-in-out` |
| `--semi-transition_function-easeOut` | `ease-out` |
| `--semi-transition_function-linear` | `linear` |
| `--semi-violet-0` | `243,237,249` / `64,27,119` |
| `--semi-violet-1` | `226,209,244` / `76,36,140` |
| `--semi-violet-2` | `196,167,233` / `88,46,160` |
| `--semi-violet-3` | `166,127,221` / `100,57,181` |
| `--semi-violet-4` | `136,91,210` / `114,70,201` |
| `--semi-violet-5` | `106,58,199` / `136,101,212` |
| `--semi-violet-6` | `87,47,179` / `162,136,223` |
| `--semi-violet-7` | `70,37,158` / `190,173,233` |
| `--semi-violet-8` | `54,28,138` / `221,212,244` |
| `--semi-violet-9` | `40,20,117` / `241,238,250` |
| `--semi-white` | `var(--white-0)` / `255,255,255` |
| `--semi-yellow-0` | `255,253,234` / `84,73,3` |
| `--semi-yellow-1` | `254,251,203` / `126,108,6` |
| `--semi-yellow-2` | `253,243,152` / `168,142,10` |
| `--semi-yellow-3` | `252,232,101` / `210,175,15` |
| `--semi-yellow-4` | `251,218,50` / `252,206,20` |
| `--semi-yellow-5` | `250,200,0` / `253,222,67` |
| `--semi-yellow-6` | `208,170,0` / `253,235,113` |
| `--semi-yellow-7` | `167,139,0` / `254,245,160` |
| `--semi-yellow-8` | `125,106,0` / `254,251,208` |
| `--semi-yellow-9` | `83,72,0` / `255,254,236` |
| `--separator-color` | `light-dark(#f0f0f4, #52525e)` / `CanvasText` |
| `--shadow-color` | `var(--skill-shadow-color,#0006)` |
| `--sidebar-backdrop-filter` | `blur(7px)` / `none` |
| `--sidebar-bg` | `var(--skill-sidebar-bg,#1a1c1e)` |
| `--sidebar-bg-color` | `light-dark(rgb(255 255 255 / 0.92), rgb(66 65 77 / 0.92))` / `var(--background-color-box, light-dark(#fff, #23222b))` / `var(--background-color-box, Canvas)` |
| `--sidebar-block-padding` | `8px` |
| `--sidebar-border-color` | `light-dark(
    rgb(21 20 26 / 0.1),
    rgb(251 251 254 / 0` / `CanvasText` |
| `--sidebar-border-radius` | `8px` |
| `--sidebar-box-shadow` | `0 0.25px 0.75px light-dark(rgb(0 0 0 / 0.05), rgb(0 0 0 / 0.` / `none` |
| `--sidebar-max-width` | `50vw` / `632px` |
| `--sidebar-min-width` | `min-content` / `180px` |
| `--sidebar-padding` | `5px` |
| `--sidebar-width` | `230px` / `239px` |
| `--signature-bg` | `var(
    --background-color-box-info,
    light-dark(#f9f9fb` / `HighlightText` |
| `--signature-border-color` | `var(--border-color-interactive, #8f8f9d)` / `var(--border-color-interactive, ButtonText)` |
| `--signature-color` | `var(--primary-color)` / `ButtonText` |
| `--signature-draw-placeholder-color` | `var(--primary-color)` |
| `--signature-hover-bg` | `var(
    --button-background-color-hover,
    light-dark(#f0` / `var(--signature-bg)` |
| `--signature-placeholder-color` | `var(--secondary-color)` |
| `--skeleton-background` | `linear-gradient(30deg,#eff3f5 20%,#f9f9f9cc 50%,#eff3f5 80%)` / `linear-gradient(30deg,#25262b 20%,#323441cc 50%,#25262b 80%)` |
| `--skill-accent` | `#00bfd1` |
| `--skill-accent-hover` | `#00a9bd` |
| `--skill-accent-soft` | `#e7f5f6` |
| `--skill-accent-text` | `#006b76` |
| `--skill-card-height` | `217px` |
| `--skill-card-min-width` | `260px` |
| `--skill-code-bg` | `#fbfcfd` |
| `--skill-composer-bg` | `#fff` |
| `--skill-composer-shadow` | `0 3px 12px #263e5010` |
| `--skill-content-width` | `100%` |
| `--skill-control-line` | `#cbd5df` |
| `--skill-danger` | `#b43c48` |
| `--skill-diff-add-bg` | `#e5f3e9` |
| `--skill-diff-remove-bg` | `#fbe8ea` |
| `--skill-history-selected` | `#d8ebed` |
| `--skill-hover` | `#142a3a0a` |
| `--skill-icon-bg` | `#e9eef2` |
| `--skill-line` | `#dfe5eb` |
| `--skill-muted` | `#526171` |
| `--skill-overlay-bg` | `#24313e52` |
| `--skill-page-bg` | `#edf1f4` |
| `--skill-panel-bg` | `#fff` |
| `--skill-popup-bg` | `#fff` |
| `--skill-scrollbar` | `#142a3a33` |
| `--skill-search-active-bg` | `#ffd268` |
| `--skill-search-bg` | `#ffe9a5` |
| `--skill-selected` | `#d8ebed` |
| `--skill-shadow-color` | `#1c354b24` |
| `--skill-sidebar-bg` | `#edf1f4` |
| `--skill-strong-line` | `#93a4b5` |
| `--skill-subtle` | `#586675` |
| `--skill-success` | `#25704b` |
| `--skill-surface` | `#f0f3f6` |
| `--skill-surface-raised` | `#e3e9ef` |
| `--skill-text` | `#202a35` |
| `--skill-timeline-effect` | `#dfe7f2` |
| `--skill-timeline-filter` | `#e9e4f5` |
| `--skill-timeline-header-effects` | `0` |
| `--skill-timeline-sticker` | `#fae7d3` |
| `--skill-timeline-template` | `#eedbd3` |
| `--skill-timeline-text` | `#f3dfd9` |
| `--skill-timeline-video` | `#dcecf3` |
| `--skill-token-boolean` | `#9b3970` |
| `--skill-token-comment` | `#596b55` |
| `--skill-token-function` | `#79611d` |
| `--skill-token-keyword` | `#7d3eb0` |
| `--skill-token-literal` | `#386d38` |
| `--skill-token-number` | `#8b571b` |
| `--skill-token-property` | `#236c98` |
| `--skill-token-string` | `#8f5727` |
| `--skill-tooltip-bg` | `#273541` |
| `--skill-tooltip-text` | `#f8fafc` |
| `--skill-turn-bg` | `#fff` |
| `--skill-turn-line` | `#dfe5eb` |
| `--skill-validation-bg` | `#f0f5f6` |
| `--skill-warning` | `#865817` |
| `--skill-workspace-bg` | `#f5f7f9` |
| `--spinner-icon` | `url(images/altText_spinner.svg)` |
| `--spreadHorizontalWrapped-margin-LR` | `-3.5px` / `3.5px` |
| `--status-actions-bg` | `light-dark(
    rgb(21 20 26 / 0.03),
    rgb(251 251 254 / ` |
| `--status-border-color` | `transparent` / `CanvasText` |
| `--status-color` | `var(--success)` / `var(--warning)` / `var(--danger)` |
| `--status-undo-bg` | `light-dark(rgb(0 98 250 / 0.08), rgb(0 202 219 / 0.08))` / `none` |
| `--status-waiting-bg` | `var(--status-undo-bg)` |
| `--status-warning-bg` | `light-dark(#ffe8ea, #6e001f)` / `none` |
| `--strong-line` | `var(--skill-strong-line,#ffffff3d)` |
| `--studio-accent` | `#7c5cff` |
| `--studio-accent-weak` | `rgba(124,92,255,.22)` |
| `--studio-bg` | `#0f1117` |
| `--studio-bg-soft` | `#151822` |
| `--studio-border` | `rgba(134,151,184,.22)` |
| `--studio-border-strong` | `rgba(144,164,203,.34)` |
| `--studio-card` | `#1b2030` |
| `--studio-card-hover` | `#22283a` |
| `--studio-danger` | `#ff6b7a` |
| `--studio-handle-offset-x` | `0px` |
| `--studio-handle-offset-y` | `0px` |
| `--studio-node-sized` | `1` |
| `--studio-panel` | `rgba(24,28,39,.92)` |
| `--studio-scrollbar-size` | `6px` |
| `--studio-scrollbar-thumb` | `hsla(0,0%,100%,.1)` |
| `--studio-scrollbar-thumb-border-width` | `1px` |
| `--studio-scrollbar-thumb-hover` | `hsla(0,0%,100%,.2)` |
| `--studio-scrollbar-thumb-radius` | `42px` |
| `--studio-shadow` | `0 24px 70px rgba(0,0,0,.42)` |
| `--studio-success` | `#41d6a5` |
| `--studio-text` | `#f4f7fb` |
| `--studio-text-muted` | `#7d8ba3` |
| `--studio-text-secondary` | `#bdc7d6` |
| `--subtle` | `var(--skill-subtle,#a2a9b3)` |
| `--success` | `var(--skill-success,#9bd7b3)` |
| `--success-1` | `var(--green-1)` |
| `--success-10` | `var(--green-10)` |
| `--success-2` | `var(--green-2)` |
| `--success-3` | `var(--green-3)` |
| `--success-4` | `var(--green-4)` |
| `--success-5` | `var(--green-5)` |
| `--success-6` | `var(--green-6)` |
| `--success-7` | `var(--green-7)` |
| `--success-8` | `var(--green-8)` |
| `--success-9` | `var(--green-9)` |
| `--surface` | `var(--skill-surface,#272a2d)` |
| `--surface-raised` | `var(--skill-surface-raised,#32363a)` |
| `--swatch-border-color` | `light-dark(#cfcfd8, #52525e)` / `ButtonText` |
| `--tab-bg` | `var(--dialog-bg-color)` / `var(--bg)` |
| `--tab-bg-active-color` | `var(--tab-bg)` / `SelectedItem` |
| `--tab-bg-active-hover-color` | `var(--bg-hover)` / `SelectedItem` |
| `--tab-bg-hover` | `var(--bg-hover)` |
| `--tab-bottom-line-active-color` | `var(--tab-top-line-inactive-color)` / `var(--tab-top-line-active-color)` |
| `--tab-bottom-line-hover-color` | `var(--tab-top-line-inactive-color)` / `var(--tab-top-line-hover-color)` |
| `--tab-bottom-line-inactive-color` | `var(--tab-top-line-inactive-color)` |
| `--tab-panel-border` | `none` / `1px solid ButtonText` |
| `--tab-panel-border-radius` | `var(--border-radius-small, 4px)` / `8px` |
| `--tab-text-active-color` | `var(--tab-top-line-active-color)` / `HighlightText` |
| `--tab-text-active-hover-color` | `var(--tab-text-hover-color)` / `HighlightText` |
| `--tab-text-color` | `var(--primary-color)` / `ButtonText` |
| `--tab-text-hover-color` | `var(--tab-text-color)` / `SelectedItem` |
| `--tab-top-line-active-color` | `var(
    --color-accent-primary,
    light-dark(#0060df, #0d` / `var(--color-accent-primary, ButtonText)` |
| `--tab-top-line-active-hover-color` | `var(--tab-text-hover-color)` / `HighlightText` |
| `--tab-top-line-hover-color` | `var(--border-color-interactive, #8f8f9d)` / `var(--border-color-interactive, SelectedItem)` |
| `--tab-top-line-inactive-color` | `light-dark(#cfcfd8, #8f8f9d)` / `ButtonText` |
| `--tabs-mask-end` | `32px` / `40px` |
| `--tabs-mask-start` | `16px` / `27px` |
| `--text` | `var(--skill-text,#e0e0e0)` |
| `--text-primary-color` | `var(--text-color, light-dark(#15141a, #fbfbfe))` / `var(--text-color, CanvasText)` |
| `--text-scale-factor` | `calc(var(--total-scale-factor) * var(--min-font-size))` |
| `--text-secondary-color` | `light-dark(#5b5b66, #cfcfd8)` / `CanvasText` |
| `--textarea-bg-color` | `light-dark(white, #42414d)` / `Field` |
| `--textarea-border-color` | `var(--border-color-interactive, #8f8f9d)` / `ButtonBorder` |
| `--textarea-fg-color` | `var(--text-secondary-color)` / `ButtonText` |
| `--thickness-bg` | `var(--dialog-bg-color)` / `Canvas` |
| `--thickness-border` | `none` / `1px solid var(--signature-border-color)` |
| `--thickness-label-color` | `var(--primary-color)` / `CanvasText` |
| `--thickness-slider-color` | `var(--primary-color)` / `ButtonText` |
| `--thumbnail-dragging-scale` | `1.4` |
| `--thumbnail-width` | `126px` |
| `--toggle-background-color` | `var(
    --button-background-color,
    color-mix(in srgb, c` / `var(--button-background-color, ButtonFace)` |
| `--toggle-background-color-active` | `var(
    --button-background-color-active,
    color-mix(in ` |
| `--toggle-background-color-hover` | `var(
    --button-background-color-hover,
    color-mix(in s` |
| `--toggle-background-color-pressed` | `var(
    --color-accent-primary,
    light-dark(#0060df, #0d` / `var(--color-accent-primary, ButtonText)` |
| `--toggle-background-color-pressed-active` | `var(
    --color-accent-primary-active,
    light-dark(#0540` / `var(
      --color-accent-primary-active,
      SelectedItem` |
| `--toggle-background-color-pressed-hover` | `var(
    --color-accent-primary-hover,
    light-dark(#0250b` / `var(
      --color-accent-primary-hover,
      SelectedItem
` |
| `--toggle-border-color` | `var(
    --border-color-interactive,
    light-dark(#8f8f9d,` / `var(--border-color-interactive, ButtonText)` |
| `--toggle-border-color-active` | `var(--toggle-border-color)` / `var(
      --border-color-interactive-active,
      ButtonTe` |
| `--toggle-border-color-hover` | `var(--toggle-border-color)` / `var(
      --border-color-interactive-hover,
      SelectedI` |
| `--toggle-border-radius` | `var(--border-radius-circle, 9999px)` |
| `--toggle-border-width` | `var(--border-width, 1px)` |
| `--toggle-dot-background-color` | `var(--toggle-border-color)` / `var(--color-accent-primary, ButtonText)` |
| `--toggle-dot-background-color-active` | `var(--toggle-dot-background-color)` / `var(
      --color-accent-primary-active,
      SelectedItem` |
| `--toggle-dot-background-color-hover` | `var(--toggle-dot-background-color)` / `var(
      --color-accent-primary-hover,
      SelectedItem
` |
| `--toggle-dot-background-color-on-pressed` | `var(
    --background-color-canvas,
    light-dark(white, #1` / `var(
      --button-background-color,
      ButtonFace
    )` |
| `--toggle-dot-height` | `calc(
    var(--toggle-height) - 2 * var(--toggle-dot-margin` |
| `--toggle-dot-margin` | `1px` |
| `--toggle-dot-transform-x` | `calc(
    var(--toggle-width) - 4 * var(--toggle-dot-margin)` |
| `--toggle-dot-width` | `var(--toggle-dot-height)` |
| `--toggle-height` | `var(--size-item-small, 16px)` |
| `--toggle-width` | `var(--size-item-large, 32px)` |
| `--token-boolean` | `var(--skill-token-boolean,#d5a1b4)` |
| `--token-comment` | `var(--skill-token-comment,#8d9f88)` |
| `--token-function` | `var(--skill-token-function,#dfcf9c)` |
| `--token-keyword` | `var(--skill-token-keyword,#c8a5e8)` |
| `--token-literal` | `var(--skill-token-literal,#a9cda0)` |
| `--token-number` | `var(--skill-token-number,#dfbd83)` |
| `--token-property` | `var(--skill-token-property,#91c7e5)` |
| `--token-string` | `var(--skill-token-string,#d8b38b)` |
| `--tooltip-bg` | `var(--skill-tooltip-bg,#32363a)` |
| `--tooltip-offset` | `4px` |
| `--tooltip-text` | `var(--skill-tooltip-text,#e0e0e0)` |
| `--total-scale-factor` | `1.5` / `calc(var(--scale-factor) * var(--user-unit))` |
| `--treeitem-bg-color` | `light-dark(rgb(0 0 0 / 0.15), rgb(255 255 255 / 0.15))` |
| `--treeitem-collapsed-icon` | `url(images/treeitem-collapsed.svg)` |
| `--treeitem-color` | `light-dark(rgb(0 0 0 / 0.8), rgb(255 255 255 / 0.8))` |
| `--treeitem-expanded-icon` | `url(images/treeitem-expanded.svg)` |
| `--treeitem-hover-color` | `light-dark(rgb(0 0 0 / 0.9), rgb(255 255 255 / 0.9))` |
| `--treeitem-selected-bg-color` | `light-dark(
    rgb(0 0 0 / 0.25),
    rgb(255 255 255 / 0.2` |
| `--treeitem-selected-color` | `light-dark(
    rgb(0 0 0 / 0.9),
    rgb(255 255 255 / 0.9)` |
| `--turn-bg` | `var(--skill-turn-bg,#202224)` |
| `--turn-line` | `var(--skill-turn-line,#ffffff1f)` |
| `--undo-label-icon` | `url(images/altText_done.svg)` |
| `--unfocus-outline` | `solid var(--outline-width) transparent` |
| `--user-unit` | `1` |
| `--validation-bg` | `var(--skill-validation-bg,#272a2d)` |
| `--video-controls-gradient` | `linear-gradient(0deg,rgba(0,0,0,.5),transparent)` / `linear-gradient(0deg,rgba(0,0,0,.3),transparent)` |
| `--video-edit-timeline-clip-audio-color` | `var(--surface)` / `#262626` |
| `--video-edit-timeline-clip-background-color` | `var(--surface-raised)` |
| `--video-edit-timeline-clip-default-stroke-color` | `var(--control-line)` / `hsla(0,0%,100%,.06)` |
| `--video-edit-timeline-clip-effect-color` | `var(--skill-timeline-effect,#3e495d)` / `#3e495d` |
| `--video-edit-timeline-clip-filter-color` | `var(--skill-timeline-filter,rgba(71,65,139,.3))` / `rgba(71,65,139,.3)` |
| `--video-edit-timeline-clip-image-color` | `var(--skill-timeline-video,#243743)` |
| `--video-edit-timeline-clip-selected-stroke-color` | `var(--accent-text)` |
| `--video-edit-timeline-clip-sticker-color` | `var(--skill-timeline-sticker,rgba(240,138,52,.3))` / `rgba(240,138,52,.3)` |
| `--video-edit-timeline-clip-text-color` | `var(--skill-timeline-text,rgba(156,73,55,.3))` / `rgba(156,73,55,.3)` |
| `--video-edit-timeline-clip-text-template-color` | `var(--skill-timeline-template,#5f4640)` / `#5f4640` |
| `--video-edit-timeline-clip-unknown-color` | `var(--surface-raised)` |
| `--video-edit-timeline-clip-video-color` | `var(--skill-timeline-video,#243743)` |
| `--video-edit-timeline-clip-waveform-color` | `var(--muted)` / `hsla(0,0%,100%,.2)` |
| `--video-edit-timeline-font-size` | `10px` |
| `--video-edit-timeline-header-effects-enabled` | `var(--skill-timeline-header-effects,1)` |
| `--video-edit-timeline-ruler-background-color` | `var(--surface)` / `transparent` |
| `--video-edit-timeline-ruler-label-color` | `var(--muted)` |
| `--video-edit-timeline-ruler-tick-color` | `var(--control-line)` |
| `--video-edit-timeline-text-color` | `var(--text)` |
| `--video-edit-timeline-track-background-color` | `var(--code-bg)` / `transparent` |
| `--video-edit-timeline-track-divider-color` | `var(--line)` |
| `--video-edit-timeline-volume-line-active-color` | `#fff` |
| `--video-edit-timeline-volume-line-color` | `#fff` |
| `--video-edit-timeline-volume-tooltip-background-color` | `rgba(48,48,48,.8)` |
| `--video-edit-timeline-volume-tooltip-text-color` | `#e0e0e0` |
| `--viewer-container-height` | `0` |
| `--views-button-border-color` | `var(--button-border-color, transparent)` / `var(--button-border-color, ButtonText)` |
| `--views-manager-add-file-button-icon` | `url(images/toolbarButton-zoomIn.svg)` |
| `--views-manager-button-arrow-icon` | `url(images/pages_viewArrow.svg)` |
| `--views-manager-button-icon` | `url(images/pages_viewButton.svg)` |
| `--views-text-color` | `var(--text-color, light-dark(#15141a, #fbfbfe))` / `var(--text-color, CanvasText)` |
| `--warning` | `var(--skill-warning,#d9bc86)` |
| `--warning-1` | `var(--orange-1)` |
| `--warning-10` | `var(--orange-10)` |
| `--warning-2` | `var(--orange-2)` |
| `--warning-3` | `var(--orange-3)` |
| `--warning-4` | `var(--orange-4)` |
| `--warning-5` | `var(--orange-5)` |
| `--warning-6` | `var(--orange-6)` |
| `--warning-7` | `var(--orange-7)` |
| `--warning-8` | `var(--orange-8)` |
| `--warning-9` | `var(--orange-9)` |
| `--white-0` | `#fafafa` |
| `--white-0-rgb` | `250,250,250` |
| `--white-00` | `#fff` |
| `--white-00-rgb` | `255,255,255` |
| `--white-0a` | `rgba(var(--white-0-rgb),0.08)` |
| `--white-1` | `#e5e5e5` |
| `--white-1-rgb` | `229,229,229` |
| `--white-1a` | `rgba(var(--white-0-rgb),0.12)` |
| `--workspace-bg` | `var(--skill-workspace-bg,#202224)` |
| `--xfa-focus-outline` | `auto` / `2px solid CanvasText` |
| `--xfa-unfocused-field-background` | `url("data:image/svg+xml` |
| `--xy-attribution-background-color-default` | `hsla(0,0%,100%,.5)` / `hsla(0,0%,59%,.25)` |
| `--xy-background-color` | `#141414` / `#101112` |
| `--xy-background-color-default` | `transparent` / `#141414` |
| `--xy-background-pattern-cross-color-default` | `#e2e2e2` / `#777` |
| `--xy-background-pattern-dots-color-default` | `#91919a` / `#777` |
| `--xy-background-pattern-lines-color-default` | `#eee` / `#777` |
| `--xy-connectionline-stroke` | `var(--canvas-connection-hover-color)` |
| `--xy-connectionline-stroke-default` | `#b1b1b7` |
| `--xy-connectionline-stroke-width-default` | `1` |
| `--xy-controls-box-shadow-default` | `0 0 2px 1px rgba(0,0,0,.08)` |
| `--xy-controls-button-background-color` | `#242728` |
| `--xy-controls-button-background-color-default` | `#fefefe` / `#2b2b2b` |
| `--xy-controls-button-background-color-hover-default` | `#f4f4f4` / `#3e3e3e` |
| `--xy-controls-button-border-color` | `#353939` |
| `--xy-controls-button-border-color-default` | `#eee` / `#5b5b5b` |
| `--xy-controls-button-color` | `#aeb5b3` |
| `--xy-controls-button-color-default` | `inherit` / `#f8f8f8` |
| `--xy-controls-button-color-hover-default` | `inherit` / `#fff` |
| `--xy-edge-label-background-color-default` | `#fff` / `#141414` |
| `--xy-edge-label-color-default` | `inherit` / `#f8f8f8` |
| `--xy-edge-stroke-default` | `#b1b1b7` / `#3e3e3e` |
| `--xy-edge-stroke-selected-default` | `#555` / `#727272` |
| `--xy-edge-stroke-width-default` | `1` |
| `--xy-handle-background-color-default` | `#1a192b` / `#bebebe` |
| `--xy-handle-border-color-default` | `#fff` / `#1e1e1e` |
| `--xy-minimap-background-color` | `#1c1f20` |
| `--xy-minimap-background-color-default` | `#fff` / `#141414` |
| `--xy-minimap-mask-background-color` | `#101112aa` |
| `--xy-minimap-mask-background-color-default` | `hsla(0,0%,94%,.6)` / `rgba(60,60,60,.6)` |
| `--xy-minimap-mask-stroke-color-default` | `transparent` |
| `--xy-minimap-mask-stroke-width-default` | `1` |
| `--xy-minimap-node-background-color-default` | `#e2e2e2` / `#2b2b2b` |
| `--xy-minimap-node-stroke-color-default` | `transparent` |
| `--xy-minimap-node-stroke-width-default` | `2` |
| `--xy-node-background-color-default` | `#fff` / `#1e1e1e` |
| `--xy-node-border-default` | `1px solid #1a192b` / `1px solid #3c3c3c` |
| `--xy-node-border-radius-default` | `3px` |
| `--xy-node-boxshadow-hover-default` | `0 1px 4px 1px rgba(0,0,0,.08)` / `0 1px 4px 1px hsla(0,0%,100%,.08)` |
| `--xy-node-boxshadow-selected-default` | `0 0 0 0.5px #1a192b` / `0 0 0 0.5px #999` |
| `--xy-node-color-default` | `inherit` / `#f8f8f8` |
| `--xy-node-group-background-color-default` | `hsla(0,0%,94%,.25)` |
| `--xy-resize-background-color-default` | `#3367d9` |
| `--xy-selection-background-color-default` | `rgba(0,89,220,.08)` / `rgba(200,200,220,.08)` |
| `--xy-selection-border-default` | `1px dotted rgba(0,89,220,.8)` / `1px dotted rgba(200,200,220,.8)` |
| `--yellow-0` | `#d4a500` |
| `--yellow-1` | `254,255,232` / `77,56,0` |
| `--yellow-10` | `77,56,0` / `254,255,240` |
| `--yellow-2` | `254,254,190` / `120,94,7` |
| `--yellow-3` | `253,250,148` / `163,134,20` |
| `--yellow-4` | `252,242,107` / `207,179,37` |
| `--yellow-5` | `251,232,66` / `250,225,60` |
| `--yellow-6` | `250,220,25` / `251,233,75` |
| `--yellow-7` | `207,175,15` / `252,243,116` |
| `--yellow-8` | `163,132,8` / `253,250,157` |
| `--yellow-9` | `120,93,3` / `254,254,198` |

## 二、调色板（按出现频次）

| 颜色 | 次数 |
| --- | ---: |
| `#fff` | 1119 |
| `#e0e0e0` | 397 |
| `#000` | 329 |
| `hsla(…, .08)` | 324 |
| `#090c14` | 277 |
| `hsla(…, .06)` | 244 |
| `#00c1cd` | 229 |
| `#949494` | 198 |
| `hsla(…, .12)` | 181 |
| `#262626` | 129 |
| `#7a7a7a` | 110 |
| `#00cae0` | 105 |
| `#fafafa` | 104 |
| `hsla(…, .9)` | 100 |
| `hsla(…, .04)` | 95 |
| `hsla(…, .2)` | 92 |
| `rgba(0,0,0,.2)` | 86 |
| `#303030` | 79 |
| `#141414` | 78 |
| `#1c1c1c` | 77 |
| `#6c6c6c` | 71 |
| `#ccc` | 69 |
| `rgba(38,38,38,.7)` | 67 |
| `hsla(…, .5)` | 59 |
| `#999` | 52 |
| `hsla(…, 0)` | 44 |
| `#d4d4d4` | 43 |
| `rgba(0,0,0,.5)` | 42 |
| `hsla(…, .07)` | 42 |
| `#3b3b3b` | 42 |
| `#070709` | 42 |
| `#e5e5e5` | 41 |
| `#b2b2b2` | 39 |
| `#646a73` | 39 |
| `hsla(…, .1)` | 38 |
| `hsla(…, .8)` | 37 |
| `#e0e8ec` | 37 |
| `#15141a` | 36 |
| `hsla(…, .25)` | 35 |
| `hsla(…, .72)` | 33 |

## 三、字号阶梯 / 行高 / 圆角 / 模糊 / 缓动

| 类目 | 取值 |
| --- | --- |
| 字号 | `12px`(1176) / `11px`(1020) / `14px`(682) / `13px`(313) / `16px`(279) / `10px`(262) / `20px`(46) / `18px`(28) / `24px`(24) / `15px`(21) / `32px`(12) / `9px`(10) / `8px`(10) / `44px`(6) / `17px`(6) / `22px`(6) / `26px`(6) / `48px`(5) / `28px`(5) / `36px`(3) |
| 圆角 | `8px`(853) / `4px`(516) / `12px`(269) / `6px`(246) / `2px`(151) / `3px`(76) / `1px`(73) / `16px`(48) / `30px`(40) / `14px`(38) / `15px`(37) / `5px`(25) / `42px`(21) / `9px`(21) / `999px`(19) |
| 背景模糊 | `24px`(94) / `48px`(70) / `20px`(42) / `5px`(34) / `40px`(10) / `10px`(8) / `8px`(4) / `3px`(4) |
| 缓动曲线 | `.3,1.3,.3,1`(367) / `.34,.69,.1,1`(360) / `0,0,1,1`(194) / `.34,1.32,.64,1`(68) / `.4,0,.2,1`(66) / `.215,.61,.355,1`(32) / `.22,1,.36,1`(31) / `.22,.57,.02,1.2`(12) |
| 字体族 | `PingFang SC` / `Inter,-apple-system,BlinkMacSystemFont,Segoe UI,Pi` / `PingFang SC,sans-serif` / `inherit` / `PingFang SC,Inter,ui-sans-serif,system-ui,sans-ser` / `PingFang SC,Inter,sans-serif` / `-apple-system,BlinkMacSystemFont,Segoe UI,PingFang` / `ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,` |

## 四、组件名（去哈希后的类名，反映界面结构）

```
semi  x2729
semi-input  x1839
lv-btn  x1147
lv-select  x1092
root  x1000
lv-input-group  x869
lv-tag  x816
semi-button  x788
semi-input-wrapper  x768
lv-menu  x708
lv-steps  x670
toolbar  x626
arco-tag  x612
lv-col  x594
lv-input  x577
lv-steps-item  x577
arco-btn  x528
lv-col-xs  x519
lv-col-sm  x519
lv-col-md  x519
lv-col-lg  x519
lv-col-xl  x519
lv-col-xxl  x519
lv-col-xxxl  x519
arco  x518
semi-checkbox-inner  x464
lv-cascader  x444
semi-avatar  x426
semi-input-wrapper__with  x420
lv-radio  x412
lv-tree-select  x404
semi-checkbox  x395
arco-select  x384
lv-tabs-header-nav  x370
semi-col  x360
semi-col-xs  x360
semi-col-sm  x360
semi-col-md  x360
semi-col-lg  x360
semi-col-xl  x360
```