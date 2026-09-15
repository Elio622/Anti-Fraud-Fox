# 音频目录

Ren'Py 标准音频目录，放游戏运行时加载的音频文件（BGM / SE）。

## 当前状态

- `options.rpy` 里 `config.has_sound = True`、`config.has_music = True` 已开启，设置界面会显示「音乐音量 / 音效音量」滑条（全部静音也可用）。
- 已加入 4 首背景音乐（BGM）+ 3 段结算音效，按剧情情绪播放：
  - `bgm_title`（主菜单/选关）、`bgm_calm`（开场日常）、`bgm_suspect`（骗子登场至抉择全程）、`bgm_relief`（识破/警察表扬通关）
  - `se_win.wav`（满分「恭喜」上升音）、`se_flat.wav`（1/2 星平缓音）、`se_fail.wav`（0 分「遗憾落败」下降音），均为原创合成
- 曲目来源与署名见仓库根目录 `CREDITS.md`（Kevin MacLeod，CC BY 4.0；结算音效为原创）。

## 使用方式

- 把处理好的 OGG / MP3 放进本目录。
- 在剧本里播放：

```renpy
play music "audio/bgm_main.ogg"   # 背景音乐
play sound "audio/se_click.ogg"   # 音效
stop music                          # 停止背景音乐
```

- 原始素材统一放在工作区 `音频/`，处理后再复制到这里。
- 音频文件名用 ASCII（英文/数字/下划线），避免中文文件名影响打包分发。
