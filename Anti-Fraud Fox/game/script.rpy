# game/script.rpy
#
# 《反诈狐》核心脚本：角色、图像、进度、路由。

## 加载界面（等待界面）
label splashscreen:
    scene black
    show bg title with fade
    $ renpy.pause(2.0)
    return


## 角色定义（白字 + 黑描边，仿 ForbiddenClaims 风格）
define mc = Character("阿狐", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="mc")
define think = Character("阿狐", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="mc", what_prefix="（", what_suffix="）")
define fraud = Character("客服", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="fraud")
define mom = Character("妈妈", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="mom")
define dad = Character("爸爸", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="dad")
define teacher = Character("老师", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="teacher")
define police = Character("反诈警察", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="police")
define n = Character(None)


## 背景与全屏图像（fit="cover" 自动缩放铺满屏幕）
image bg title = Transform("images/title.jpg", xsize=1280, ysize=720)
image bg clear1 = Transform("images/clear1.png", xsize=1280, ysize=720)
image bg clear2 = Transform("images/clear2.png", xsize=1280, ysize=720)
image bg clear3 = Transform("images/clear3.png", xsize=1280, ysize=720)
image bg fail = Transform("images/fail.png", xsize=1280, ysize=720)
image bg bedroom = Transform("images/bg_bedroom.png", xsize=1280, ysize=720)
image bg living = Transform("images/bg_living.png", xsize=1280, ysize=720)

## 关卡1 剧情插图 / 手机界面
image l1_find_mom = Transform("images/l1_find_mom.jpg", xsize=1280, ysize=720)
image l1_bedroom_play = Transform("images/l1_bedroom_play.jpg", xsize=1280, ysize=720)
image l1_bedroom_deceived = Transform("images/l1_bedroom_deceived.jpg", xsize=1280, ysize=720)
image l1_block = Transform("images/l1_block.png", xsize=1280, ysize=720)
image l1_submit_fail = Transform("images/l1_submit_fail.png", xsize=1280, ysize=720)
image l1_final = Transform("images/l1_final.png", xsize=1280, ysize=720)
image l1_msg = Transform("images/l1_msg.png", xsize=1280, ysize=720)
image l1_deceived = Transform("images/l1_deceived.png", xsize=1280, ysize=720)
image l1_police = Transform("images/l1_police.png", xsize=1280, ysize=720)
image l1_claim = Transform("images/l1_claim.png", xsize=1280, ysize=720)
image l1_chat = Transform("images/l1_chat.png", xsize=1280, ysize=720)
image l1_restore = Transform("images/l1_restore.png", xsize=1280, ysize=720)
image l1_mom_comfort = Transform("images/l1_mom_comfort.png", xsize=1280, ysize=720)


## 角色立绘（共用 side 标签，show 时自动替换上一个角色）
## 主角小狐狸「阿狐」的表情立绘（已抠透明底）
image side mc = "images/mc_normal.png"
image side mc normal = "images/mc_normal.png"
image side mc serious = "images/mc_serious.png"
image side mc laugh = "images/mc_laugh.png"
image side mc worried = "images/mc_worried.png"
image side mc sad = "images/mc_sad.png"
image side mc confused = "images/mc_confused.png"

## 其他角色的表情立绘（已抠透明底）
## 客服（浣熊诈骗犯）
image side fraud = "images/fraud_normal.png"
image side fraud normal = "images/fraud_normal.png"
image side fraud serious = "images/fraud_serious.png"
image side fraud laugh = "images/fraud_laugh.png"
image side fraud worried = "images/fraud_worried.png"
image side fraud sad = "images/fraud_sad.png"
image side fraud suspicious = "images/fraud_suspicious.png"

## 妈妈（小狐狸母亲）
image side mom = "images/mom_normal.png"
image side mom normal = "images/mom_normal.png"
image side mom serious = "images/mom_serious.png"
image side mom laugh = "images/mom_laugh.png"
image side mom worried = "images/mom_worried.png"
image side mom sad = "images/mom_sad.png"
image side mom confused = "images/mom_confused.png"

## 爸爸（小狐狸父亲）
image side dad = "images/dad_normal.png"
image side dad normal = "images/dad_normal.png"
image side dad serious = "images/dad_serious.png"
image side dad laugh = "images/dad_laugh.png"
image side dad worried = "images/dad_worried.png"
image side dad sad = "images/dad_sad.png"
image side dad confused = "images/dad_confused.png"

## 老师（猫头鹰老师）
## 翅膀展开较宽（原图 2175px），zoom 0.84 时屏显约 155px、右缘 x≈255，仍压住名字框（x=240 起）并逼近正文左界 268；
## 再降至 zoom 0.70：屏显约 129px、右缘 x≈229，完全让出名字框与对话正文（正文左界 x=268）。
image side teacher = Transform("images/teacher_normal.png", zoom=0.70)
image side teacher normal = Transform("images/teacher_normal.png", zoom=0.70)
image side teacher serious = Transform("images/teacher_serious.png", zoom=0.70)
image side teacher laugh = Transform("images/teacher_laugh.png", zoom=0.70)
image side teacher worried = Transform("images/teacher_worried.png", zoom=0.70)
image side teacher sad = Transform("images/teacher_sad.png", zoom=0.70)
image side teacher suspicious = Transform("images/teacher_suspicious.png", zoom=0.70)

## 反诈警察（狗狗警长）
image side police = "images/police_normal.png"
image side police normal = "images/police_normal.png"
image side police serious = "images/police_serious.png"
image side police laugh = "images/police_laugh.png"
image side police sad = "images/police_sad.png"
image side police suspicious = "images/police_suspicious.png"
image side police confused = "images/police_confused.png"

## 小兔（阿狐的同学，ch03 冒充同学案受害人）
## 小兔耳朵展开特别宽（原图 2265px），附加 zoom 0.81 缩小屏显宽度，
## 使其右缘不超过对话文本左界（x=268），避免遮挡文字。
image side rabbit = Transform("images/rabbit.png", zoom=0.81)
image side rabbit normal = Transform("images/rabbit_normal.png", zoom=0.81)
image side rabbit serious = Transform("images/rabbit_serious.png", zoom=0.81)
image side rabbit laugh = Transform("images/rabbit_laugh.png", zoom=0.81)
image side rabbit worried = Transform("images/rabbit_worried.png", zoom=0.81)
image side rabbit sad = Transform("images/rabbit_sad.png", zoom=0.81)
image side rabbit suspicious = Transform("images/rabbit_suspicious.png", zoom=0.81)
image side rabbit confused = Transform("images/rabbit_confused.png", zoom=0.81)


## 对话框左侧立绘（缩小、底部对齐）
transform side_portrait:
    xalign 0.0
    yalign 1.0
    xoffset 100
    yoffset -40
    zoom 0.085


## 关卡名称（选关界面用）
init python:
    CHAPTER_NAMES = [
        "免费皮肤", "点赞返利", "冒充同学", "快递中奖",
        "网课退费", "粉丝福利", "租号卖号", "虚假网购",
        "冒充公检法", "私密照勒索", "刷单垫资", "校园贷",
        "虚假中奖", "AI换脸冒充", "终极试炼",
    ]


## 进度（持久化）
init python:
    if persistent.unlocked is None:
        persistent.unlocked = 1
    if persistent.stars is None:
        persistent.stars = {}
    # 早期版本为 5 星制，旧存档可能存了 5 星；统一把星级修正到 3 星以内
    persistent.stars = {k: min(v, 3) for k, v in dict(persistent.stars).items()}


## 通关记录函数：通关本关并记录最佳星级
init python:
    def clear_chapter(ch, stars):
        if persistent.unlocked <= ch:
            persistent.unlocked = ch + 1
        d = dict(persistent.stars)
        key = str(ch)
        if stars > d.get(key, 0):
            d[key] = stars
        persistent.stars = d


## 游戏入口：进入选关
label start:
    jump select_level


label select_level:
    $ quick_menu = False
    window hide
    $ _level = renpy.call_screen("level_select")
    $ quick_menu = True
    if _level is None:
        return
    # 进入新关卡前清空对话历史，避免上一关的对话残留到下一关（重试同理）
    $ _history_list = []
    jump expression "ch%d" % _level


## 第 2 关占位（第 1、3~15 关已有剧本；占位关按 1 星通过，保证关卡链可以继续解锁）
label ch2:
    $ clear_chapter(2, 1)
    n "第 2 关还在开发中，敬请期待！"
    jump select_level
