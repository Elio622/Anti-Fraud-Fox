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

## 关卡2 剧情插图 / 手机界面
image l2_bedroom = Transform("images/l2_bedroom.png", xsize=1280, ysize=720)
image l2_video = Transform("images/l2_video.png", xsize=1280, ysize=720)
image l2_msg = Transform("images/l2_msg.png", xsize=1280, ysize=720)
image l2_skip = Transform("images/l2_skip.png", xsize=1280, ysize=720)
image l2_mom_phone = Transform("images/l2_mom_phone.png", xsize=1280, ysize=720)
image l2_mom_explain = Transform("images/l2_mom_explain.png", xsize=1280, ysize=720)
image l2_mom_comfort = Transform("images/l2_mom_comfort.png", xsize=1280, ysize=720)
image l2_transfer = Transform("images/l2_transfer.png", xsize=1280, ysize=720)
image l2_pay = Transform("images/l2_pay.png", xsize=1280, ysize=720)
image l2_blocked = Transform("images/l2_blocked.png", xsize=1280, ysize=720)
image l2_block = Transform("images/l2_block.png", xsize=1280, ysize=720)
image l2_teacher_call = Transform("images/l2_teacher_call.png", xsize=1280, ysize=720)
image l2_refuse = Transform("images/l2_refuse.png", xsize=1280, ysize=720)
image l2_retain = Transform("images/l2_retain.png", xsize=1280, ysize=720)
image l2_delete = Transform("images/l2_delete.png", xsize=1280, ysize=720)
image l2_police_station = Transform("images/l2_police_station.png", xsize=1280, ysize=720)
image l2_voice_teacher = Transform("images/l2_voice_teacher.png", xsize=1280, ysize=720)
image l2_forward = Transform("images/l2_forward.png", xsize=1280, ysize=720)
image l2_forward_req = Transform("images/l2_forward_req.png", xsize=1280, ysize=720)

## 关卡3 剧情插图（冒充同学诈骗）
image l3_chat_msg = Transform("images/l3_chat_msg.png", xsize=1280, ysize=720)
image l3_rabbit_800 = Transform("images/l3_rabbit_800.png", xsize=1280, ysize=720)
image l3_qrcode_pay = Transform("images/l3_qrcode_pay.png", xsize=1280, ysize=720)
image l3_payment_confirm = Transform("images/l3_payment_confirm.png", xsize=1280, ysize=720)
image l3_payment_confirm_100 = Transform("images/l3_payment_confirm_100.png", xsize=1280, ysize=720)
image l3_phone_verify = Transform("images/l3_phone_verify.png", xsize=1280, ysize=720)
image l3_video_refused = Transform("images/l3_video_refused.png", xsize=1280, ysize=720)
image l3_blocked_account = Transform("images/l3_blocked_account.png", xsize=1280, ysize=720)
image l3_final_summary = Transform("images/l3_final_summary.png", xsize=1280, ysize=720)
image rabbit_full_normal = Transform("images/rabbit_full_normal.png", xsize=1280, ysize=720)
image rabbit_full_cute = Transform("images/rabbit_full_cute.png", xsize=1280, ysize=720)

## 关卡5 剧情分镜
image l5_homework = Transform("images/l5_00_homework.png", xsize=1280, ysize=720)
image l5_refund_message = Transform("images/l5_01_refund_message.png", xsize=1280, ysize=720)
image l5_ask_mom = Transform("images/l5_02_ask_mom.png", xsize=1280, ysize=720)
image l5_fake_group = Transform("images/l5_03_fake_group.png", xsize=1280, ysize=720)
image l5_app_request = Transform("images/l5_04_app_request.png", xsize=1280, ysize=720)
image l5_show_evidence = Transform("images/l5_05_show_evidence.png", xsize=1280, ysize=720)
image l5_refuse_app = Transform("images/l5_06_refuse_app.png", xsize=1280, ysize=720)
image l5_register = Transform("images/l5_07_register.png", xsize=1280, ysize=720)
image l5_unfreeze_500 = Transform("images/l5_08_unfreeze_500.png", xsize=1280, ysize=720)
image l5_mom_help = Transform("images/l5_09_mom_help.png", xsize=1280, ysize=720)
image l5_small_reward = Transform("images/l5_10_small_reward.png", xsize=1280, ysize=720)
image l5_task_3000 = Transform("images/l5_11_task_3000.png", xsize=1280, ysize=720)
image l5_stop_payment = Transform("images/l5_12_stop_payment.png", xsize=1280, ysize=720)
image l5_payment_trap = Transform("images/l5_13_payment_trap.png", xsize=1280, ysize=720)
image l5_contact_lost = Transform("images/l5_14_contact_lost.png", xsize=1280, ysize=720)
image l5_mom_comfort = Transform("images/l5_15_mom_comfort.png", xsize=1280, ysize=720)

## 关卡6 剧情分镜
image l6_anniversary_night = Transform("images/l6_01_anniversary_night.png", xsize=1280, ysize=720)
image l6_fake_giveaway = Transform("images/l6_02_fake_giveaway.png", xsize=1280, ysize=720)
image l6_exit_and_report = Transform("images/l6_03_exit_and_report.png", xsize=1280, ysize=720)
image l6_question_qr = Transform("images/l6_04_question_qr.png", xsize=1280, ysize=720)
image l6_fake_proof = Transform("images/l6_05_fake_proof.png", xsize=1280, ysize=720)
image l6_identity_request = Transform("images/l6_06_identity_request.png", xsize=1280, ysize=720)
image l6_ask_mom = Transform("images/l6_07_ask_mom.png", xsize=1280, ysize=720)
image l6_refuse_identity = Transform("images/l6_08_refuse_identity.png", xsize=1280, ysize=720)
image l6_submit_information = Transform("images/l6_09_submit_information.png", xsize=1280, ysize=720)
image l6_authentication_fee = Transform("images/l6_10_authentication_fee.png", xsize=1280, ysize=720)
image l6_enter_lottery_group = Transform("images/l6_11_enter_lottery_group.png", xsize=1280, ysize=720)
image l6_fake_winner = Transform("images/l6_12_fake_winner.png", xsize=1280, ysize=720)
image l6_stop_before_payment = Transform("images/l6_13_stop_before_payment.png", xsize=1280, ysize=720)
image l6_customs_fee_trap = Transform("images/l6_14_customs_fee_trap.png", xsize=1280, ysize=720)
image l6_blocked_after_payments = Transform("images/l6_15_blocked_after_payments.png", xsize=1280, ysize=720)
image l6_mom_comfort = Transform("images/l6_16_mom_comfort.png", xsize=1280, ysize=720)

## 关卡13 剧情分镜
image l13_game_night = Transform("images/l13_01_game_night.png", xsize=1280, ysize=720)
image l13_jackpot_popup = Transform("images/l13_02_jackpot_popup.png", xsize=1280, ysize=720)
image l13_claim_registration = Transform("images/l13_03_claim_registration.png", xsize=1280, ysize=720)
image l13_stop_at_fee = Transform("images/l13_04_stop_at_fee.png", xsize=1280, ysize=720)
image l13_close_and_report = Transform("images/l13_05_close_and_report.png", xsize=1280, ysize=720)
image l13_question_the_fee = Transform("images/l13_06_question_the_fee.png", xsize=1280, ysize=720)
image l13_fake_evidence = Transform("images/l13_07_fake_evidence.png", xsize=1280, ysize=720)
image l13_ask_mom = Transform("images/l13_08_ask_mom.png", xsize=1280, ysize=720)
image l13_refuse_and_leave = Transform("images/l13_09_refuse_and_leave.png", xsize=1280, ysize=720)
image l13_information_leaked = Transform("images/l13_10_information_leaked.png", xsize=1280, ysize=720)
image l13_pay_notary_fee = Transform("images/l13_11_pay_notary_fee.png", xsize=1280, ysize=720)
image l13_tax_threat = Transform("images/l13_12_tax_threat.png", xsize=1280, ysize=720)
image l13_wake_up_and_report = Transform("images/l13_13_wake_up_and_report.png", xsize=1280, ysize=720)
image l13_partial_tax_trap = Transform("images/l13_14_partial_tax_trap.png", xsize=1280, ysize=720)
image l13_blocked_after_payments = Transform("images/l13_15_blocked_after_payments.png", xsize=1280, ysize=720)
image l13_confess_and_call_police = Transform("images/l13_16_confess_and_call_police.png", xsize=1280, ysize=720)

## 关卡14 剧情分镜
image l14_homework_alone = Transform("images/l14_01_homework_alone.png", xsize=1280, ysize=720)
image l14_dad_video_call = Transform("images/l14_02_dad_video_call.png", xsize=1280, ysize=720)
image l14_fake_dad_hotel = Transform("images/l14_03_fake_dad_hotel.png", xsize=1280, ysize=720)
image l14_secret_transfer_demand = Transform("images/l14_04_secret_transfer_demand.png", xsize=1280, ysize=720)
image l14_hang_up_and_callback = Transform("images/l14_05_hang_up_and_callback.png", xsize=1280, ysize=720)
image l14_question_details = Transform("images/l14_06_question_details.png", xsize=1280, ysize=720)
image l14_vague_pressure = Transform("images/l14_07_vague_pressure.png", xsize=1280, ysize=720)
image l14_verify_with_family = Transform("images/l14_08_verify_with_family.png", xsize=1280, ysize=720)
image l14_family_code_test = Transform("images/l14_09_family_code_test.png", xsize=1280, ysize=720)
image l14_mom_stops_password = Transform("images/l14_10_mom_stops_password.png", xsize=1280, ysize=720)
image l14_take_moms_phone = Transform("images/l14_11_take_moms_phone.png", xsize=1280, ysize=720)
image l14_payment_password = Transform("images/l14_12_payment_password.png", xsize=1280, ysize=720)
image l14_stop_before_password = Transform("images/l14_13_stop_before_password.png", xsize=1280, ysize=720)
image l14_partial_transfer_2000 = Transform("images/l14_14_partial_transfer_2000.png", xsize=1280, ysize=720)
image l14_full_transfer_blocked = Transform("images/l14_15_full_transfer_blocked.png", xsize=1280, ysize=720)
image l14_family_safety_code = Transform("images/l14_16_family_safety_code.png", xsize=1280, ysize=720)


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
    if renpy.music.get_playing() != "audio/bgm_title.mp3":
        play music "audio/bgm_title.mp3" fadein 1.0 fadeout 1.0
    $ quick_menu = False
    window hide
    $ _level = renpy.call_screen("level_select")
    $ quick_menu = True
    if _level is None:
        return
    # 进入新关卡前清空对话历史，避免上一关的对话残留到下一关（重试同理）
    $ _history_list = []
    jump expression "ch%d" % _level
