# game/ch01.rpy
#
# 关卡1：免费游戏皮肤诈骗

define l1_tip = "游戏福利多陷阱，私信免费不可信，不填密码不扫码，遇事先找父母亲！"


label ch1:
    play music "audio/bgm_calm.mp3" fadein 1.0 fadeout 1.0

    # === 前置剧情 ===
    scene l1_bedroom_play
    n "周五的傍晚，作业全部完成，终于到了轻松的游戏时间。"
    n "阿狐和班里大多数同学一样，喜欢玩一款休闲小游戏。看着同学们炫酷的限定皮肤、专属游戏特效，心里一直很羡慕。"
    n "可正版皮肤价格很贵，他从来不舍得让爸爸妈妈花钱买。这一份小小的期待，悄悄被网络里的骗子盯上了。"

    scene l1_bedroom_play
    n "阿狐坐在书桌前，点开手机游戏，熟练打完一把对局，返回游戏大厅。"

    scene l1_msg
    n "游戏私信红点闪烁，陌生用户发来好友申请与私信——对方头像带着官方标识，昵称：游戏福利客服06号。"

    # === 第一幕 · 初次诱骗 ===
    fraud laugh "同学你好！系统检测到你是长期活跃优质玩家！本周末开启学生专属免费福利活动，绝版限定皮肤+1000点券全程0元领取，不充值、不花钱，仅限未成年学生！"
    fraud laugh "名额仅剩最后3位，我专门为你保留了通道，错过永久绝版！"

    play music "audio/bgm_suspect.mp3" fadein 1.0 fadeout 1.0
    menu:
        "有点心动，回复询问：真的免费吗？需要我做什么才能领？":
            jump ch1_B
        "直接拒绝好友申请，拉黑并举报对方账号":
            jump ch1_A
        "立刻同意好友申请，主动追问领取方式":
            jump ch1_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch1_A:
    scene l1_bedroom_play
    n "阿狐眼神坚定，想起学校反诈班会的内容，毫不犹豫点击「拒绝申请」，一键拉黑、举报违规用户。"
    think serious "学校反诈班会教过我，天上不会掉馅饼，这种私聊就是陷阱！"
    mc serious "天下没有免费的皮肤，官方不会私下找我送福利。"

    scene l1_restore
    n "陌生私信消失，游戏界面恢复干净，无任何骚扰。"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police laugh "小朋友太棒了！正规游戏官方的所有福利，只会发布在游戏官方活动页面，任何私人私信、陌生客服私聊送皮肤、送点券，全部都是诈骗陷阱。不贪心、不搭理、直接举报，就是保护自己最好的方式！"

    $ clear_chapter(1, 3)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_win.wav"
    call screen level_clear(1, 3, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二幕 ============
label ch1_B:
    scene l1_msg
    n "阿狐眼睛一亮，心生期待，手指打字回复对方。"
    think laugh "要是能白拿限定皮肤，那也太好了！"
    mc confused "真的全部免费吗？我需要做什么才能领到限定皮肤？"

    fraud laugh "百分百真实！专门给没有零花钱的小学生准备的福利，不用充值、不用花钱，只需要简单登记一下信息就可以秒到账！好多你们学校的同学都领完了，你看这是大家的到账截图！"
    scene l1_chat
    n "对方连续发送多张高仿官方截图、虚假用户领取反馈图、活动海报，画面逼真、极具迷惑性。"
    fraud serious "最后两个名额了！你快点操作，晚一秒就被别人抢光，以后再也没有免费皮肤活动了！"

    menu:
        "点击对方发来的福利链接，查看活动页面":
            jump ch1_B2
        "相信截图，准备填写个人信息领皮肤":
            jump ch1_B3
        "关掉私信页面，找妈妈帮忙核实真假":
            jump ch1_B1


# B1：求助家长 · 满分
label ch1_B1:
    scene l1_find_mom
    n "阿狐压住心里的期待，克制住好奇心，直接退出游戏私信，拿着手机走到客厅找到妈妈。"
    think worried "虽然很想要皮肤，但总觉得不太对劲，还是先问问妈妈吧。"
    mc worried "妈妈，你看有人私聊我说可以免费领游戏皮肤，是真的吗？"

    mom serious "宝贝，这是专门骗小朋友的骗局哦。游戏官方不会私下找人送皮肤，这些截图都是骗子伪造的。遇到这种陌生免费福利，一定不能自己乱操作，先来问爸爸妈妈就对了。"
    n "妈妈指导阿狐删除链接、举报账号、清理陌生私信。"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police laugh "遇到陌生福利不慌张，先停顿、不操作、问家长，这是中小学生最靠谱的反诈方式！你做得非常优秀！"

    $ clear_chapter(1, 3)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_win.wav"
    call screen level_clear(1, 3, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# B2：好奇点链接 · 及时止损（2星）
label ch1_B2:
    scene l1_claim
    n "阿狐忍不住好奇，点击对方发送的陌生外链。"
    n "手机跳转至高仿官方网页，页面logo、配色、排版和正版游戏几乎一模一样，顶部写着：学生专属福利领取中心。页面提示：填写游戏账号、手机号即可领取绝版皮肤。"

    n "阿狐仔细观察，发现这是浏览器外部网页，不是游戏内置官方弹窗，瞬间产生警惕，立刻关闭网页、退出游戏登录。"
    think serious "不对，这是浏览器外面的网页，肯定不是官方，我得赶紧告诉妈妈！"
    mc serious "这个页面不是官方的，不对劲，我要告诉妈妈！"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police serious "陌生外链都是骗子制作的钓鱼假页面，专门盗取小朋友的账号和个人信息。你能够及时发现异常、立刻停止操作，成功守住了自己的账号安全！"

    $ clear_chapter(1, 2)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_flat.wav"
    call screen level_clear(1, 2, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# B3：填写信息 · 轻微泄露（1星）
label ch1_B3:
    scene l1_claim
    n "阿狐完全相信虚假截图，在钓鱼网页认真填写了自己的游戏账号和手机号码。"

    fraud laugh "信息收到啦！还差一个短信验证码，你把收到的验证码发给我，皮肤立刻秒到账！"

    n "阿狐正要查看短信，突然想起老师的反诈课堂：任何人索要短信验证码都是骗子！"
    think serious "老师说过，谁要验证码谁就是骗子！"
    mc serious "我不能给你验证码，你是骗子！"

    scene l1_find_mom
    n "阿狐立刻退出页面，不再回复，拿着手机找到家长说明情况。家长第一时间修改游戏密码，屏蔽陌生骚扰。"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police serious "随意填写账号和手机号，会造成个人信息泄露，引来后续诈骗和骚扰。好在你及时醒悟、终止操作，没有造成更大的损失！"

    $ clear_chapter(1, 1)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_flat.wav"
    call screen level_clear(1, 1, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三幕 ============
label ch1_C:
    scene l1_msg
    n "阿狐极度想要绝版皮肤，担心名额被抢，快速同意好友申请，主动打字追问。"
    think laugh "绝版皮肤我来了，一定不能让别人抢走！"
    mc laugh "你好！我想要限定皮肤，怎么才能领取？我很快的！"

    fraud laugh "我特别理解！小朋友没有零花钱买皮肤，所以官方专门开了学生免费通道！全程不收费、不坑人，很多小学生都领到了专属特效和点券，你放心操作！"

    scene l1_claim
    n "对方发送钓鱼链接，弹出领取硬性要求。"
    fraud serious "必须填写游戏账号、登录密码、短信验证码三项信息，系统才能绑定账号发放皮肤，少一项都无法发货！"

    menu:
        "猛然醒悟，放弃福利，删除拉黑举报翻盘":
            jump ch1_C1
        "心存侥幸，只填账号手机号，不填密码验证码":
            jump ch1_C2
        "全部如实填写，等待皮肤到账":
            jump ch1_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch1_C1:
    scene l1_claim
    n "手指悬在输入框上，即将点击提交，脑海中突然响起反诈口诀：天下没有免费的午餐！免费皮肤全是陷阱！"
    think serious "等等！天下没有免费的午餐，这一定有问题！"
    mc serious "我不要免费皮肤了，你是骗子！"

    scene l1_restore
    n "阿狐果断关闭网页，删除好友、拉黑账号、一键举报，主动把整件事告诉妈妈和班主任。"

    mom laugh "你能抵住诱惑、及时醒悟，真的非常棒！"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police serious "面对唾手可得的诱惑，能够坚守底线、及时止损，是非常优秀的反诈素养！所有诈骗，都是从贪图小便宜开始的！"

    $ clear_chapter(1, 3)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_win.wav"
    call screen level_clear(1, 3, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch1_C2:
    scene l1_claim
    n "既想要皮肤，又害怕被骗，心存侥幸。阿狐只填写游戏账号和手机号，刻意避开密码和验证码。"

    scene l1_submit_fail
    n "诈骗分子获取基础信息后，尝试登录账号失败，开始疯狂发送诈骗短信、陌生福利链接、小号骚扰。"

    mc sad "怎么一直有奇怪的消息，好烦！"

    scene l1_find_mom
    n "阿狐不堪其扰，拿着手机去找妈妈求助。妈妈帮忙屏蔽骚扰、加固账号安全。"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police serious "没有「只填一点信息没事」的骗局！只要泄露个人信息，就会给骗子留下可乘之机，引来二次诈骗和无休止骚扰。"

    $ clear_chapter(1, 1)
    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_flat.wav"
    call screen level_clear(1, 1, l1_tip)
    stop sound
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch1_C3:
    scene l1_claim
    n "满心欢喜、毫无防备，一心只想拿到绝版皮肤。阿狐认真完整填写游戏账号、登录密码、手机验证码，点击提交。"

    scene l1_deceived
    n "页面瞬间黑屏、刷新、所有福利提示全部消失。"

    scene l1_bedroom_deceived
    n "阿狐立刻返回游戏，发现账号被强制下线，再次登录提示密码错误。"

    scene l1_block
    n "打开聊天框，发现自己已被对方拉黑，好友、私信全部清空。账号内所有皮肤、点券、道具、碎片全部被盗号者清空。"

    mc sad "我不该相信免费皮肤的，我被骗了……"
    n "阿狐主动向妈妈坦白全部经过，诚恳认错。"

    scene l1_mom_comfort
    mom normal "没关系，这次经历也是一次成长。天上不会掉免费的礼物，以后遇到这种福利我们坚决不相信就好。"

    play music "audio/bgm_relief.mp3" fadein 1.0 fadeout 1.0
    scene l1_police
    police serious "小朋友一定要记住！任何索要游戏密码、手机验证码的免费福利，百分百是诈骗！游戏官方永远不会私下索要你的私密账号信息。贪图免费道具，最后只会丢失账号和个人信息。"

    $ quick_menu = False
    stop music fadeout 0.5
    play sound "audio/se_fail.wav"
    call screen level_fail(1, l1_tip)
    stop sound
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch1
    else:
        jump select_level
