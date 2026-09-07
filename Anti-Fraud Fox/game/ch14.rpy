# game/ch14.rpy
#
# 关卡14：AI换脸冒充诈骗（假「爸爸」视频通话）
#
# 骗子用AI换脸冒充「爸爸」，因此本关直接借用 dad 角色呈现以假乱真的视频画面。
define l14_tip = "眼见不一定为实，AI换脸能造假，挂断回拨再核实，全家约定安全暗号！"


label ch14:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周三晚上，爸爸出差在外地，妈妈加班还没回来，阿狐独自在家写作业。"
    n "八点整，平板突然响起来电铃声——屏幕上跳出「爸爸」的名字和头像，是视频通话。"
    n "接通后，画面里出现爸爸的脸，背景看起来像酒店房间。"
    dad serious "阿狐，是爸爸。别开声外放，我有急事跟你说。"

    # === 第一轮抉择 ===
    dad serious "爸爸刚才开车不小心蹭到了人，对方开口要2万私了，不然就要报警扣车。爸爸卡里钱不够，急用钱，这事先别告诉你妈，她胆子小会慌。"
    dad serious "你用你妈手机的支付密码，先把钱转给对方账号，明天爸爸回去补上，千万保密！"

    menu:
        "觉得不对劲：这么大的事怎么会瞒着妈妈？":
            jump ch14_A
        "心里发慌，追问事情的具体细节":
            jump ch14_B
        "救爸爸要紧，去找妈妈的手机":
            jump ch14_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch14_A:
    scene bg_bedroom
    n "画面里爸爸的脸、声音都对，可「瞒着妈妈转2万」这个要求，让阿狐心里咯噔一下。"
    think serious "爸爸说过，家里大事小事从来都是两个人商量，真出车祸第一件事是报警和保险，绝不会只瞒着我一个人！老师还讲过AI换脸骗局……"
    mc serious "爸，这么大的事不能瞒着妈妈。你先挂了，我打你手机确认一下。"
    n "阿狐挂断视频，立刻拨打爸爸的手机号——爸爸正在外地开会，手机通了，他说根本没打过视频，也没出任何事故！"
    dad laugh "儿子，有人用AI换脸冒充爸爸行骗！你做得太对了，钱一分都不能转，把通话记录截图发给妈妈，我们马上报警。"

    scene bg_living
    police laugh "教科书级别的处理！AI能造假脸、造假声，但造假不了「回拨核实」。记住：涉及转账的视频电话，一律挂断，回拨本人号码确认！"

    $ clear_chapter(14, 3)
    $ quick_menu = False
    call screen level_clear(14, 3, l14_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch14_B:
    scene bg_bedroom
    mc confused "你在哪个城市？蹭到人了怎么不报警走保险？对方怎么开口就是2万？"
    dad serious "别问那么多！对方是本地混混，报警只会更麻烦，私了最省事！爸爸赶时间，两万块晚一分都不行！"
    n "对方的回答含糊其辞，只会催着转钱。"
    dad serious "你要是心疼爸爸，就别磨蹭！用妈妈的手机转，账号我现在发给你！"

    menu:
        "挂断电话，联系妈妈和爸爸本人核实":
            jump ch14_B1
        "提出「家庭暗号」问题，验证真假":
            jump ch14_B2
        "怕耽误救急，去拿妈妈的手机":
            jump ch14_B3


# B1：联系家人核实 · 满分
label ch14_B1:
    scene bg_living
    n "阿狐越听越心慌，但「不许问、快转钱」的态度让他起了疑心。"
    think worried "视频里明明是爸爸，可他答不上任何细节，只会催钱……不行，先核实！"
    n "阿狐挂断视频，先给妈妈打电话说明情况，又拨打爸爸手机。爸爸说根本没出事，也提醒他这是新型AI诈骗。"
    mom serious "宝贝，这是「AI换脸」骗局！以后遇到视频借钱的，先挂断、再回拨、问细节，三步缺一不可。"
    n "一家人连夜把通话记录交给警察，并约定了只有全家知道的安全暗号。"

    scene bg_bedroom
    police laugh "先核实、再行动，满分！AI换脸骗得了眼睛，骗不了核实。凡是视频、电话里谈到钱的，挂断回拨，一个细节都别放过！"

    $ clear_chapter(14, 3)
    $ quick_menu = False
    call screen level_clear(14, 3, l14_tip)
    $ quick_menu = True
    jump select_level


# B2：家庭暗号验证 · 及时止损（2星）
label ch14_B2:
    scene bg_bedroom
    mc serious "那你说说，我们家的安全暗号是什么？上个月全家去哪儿玩的？"
    dad serious "暗号？什么暗号？上个月……不就是出去玩了吗！你别问这些没用的，快转钱！"
    think serious "答不上暗号，也说不出去了哪儿——视频里的「爸爸」是假的！"
    mc serious "我爸不可能答不上暗号。你是用AI换脸的骗子！"
    n "阿狐挂断视频并拉黑。他马上联系妈妈，妈妈核实后确认爸爸平安无事。"
    n "一家人把聊天记录交给警察，并更新了安全暗号。"

    scene bg_living
    police serious "「安全暗号」用得好！假脸能造，假声音能仿，但骗子猜不出你家的秘密约定。建议每个家庭都设一个暗号，专门用来核实身份！"

    $ clear_chapter(14, 2)
    $ quick_menu = False
    call screen level_clear(14, 2, l14_tip)
    $ quick_menu = True
    jump select_level


# B3：被画面骗住 · 轻微泄露（1星）
label ch14_B3:
    scene bg_bedroom
    n "画面和声音实在太像爸爸了，阿狐相信了大半，蹑手蹑脚去拿妈妈的手机。"
    n "支付页面要求输入密码，阿狐试着输了一遍妈妈的常用密码——错误；又试了一遍，还是错误。"
    n "第三次输入时，妈妈加班回来了，一把按住手机：你在干什么？！"
    n "听阿狐讲完，妈妈立刻回拨爸爸电话核实——果然是AI换脸骗局，根本没出车祸。"
    mom serious "太危险了！你已经摸到支付环节了！以后谁在视频里让你转账，先挂断、再回拨，密码谁都不能试！"

    scene bg_bedroom
    police serious "好险！幸好支付密码没试出来，不然两万块就没了。记住：AI换脸骗局的最后一步永远是「密码」和「转账」，这两道门谁也敲不开！"

    $ clear_chapter(14, 1)
    $ quick_menu = False
    call screen level_clear(14, 1, l14_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch14_C:
    scene bg_bedroom
    n "阿狐一心想着「救爸爸」，轻手轻脚拿到了妈妈的手机。"
    think laugh "爸爸平时最疼我了，这次换我救他！"
    mc laugh "爸，我拿到妈妈的手机了，账号多少？我马上转！"
    dad serious "好儿子！账号我发你，先转2万。转完删掉记录，千万别让你妈发现！"
    n "对方发来一个陌生账户。阿狐输入转账金额，页面弹出支付密码输入框。"

    menu:
        "输密码前猛然醒悟，停下一切操作":
            jump ch14_C1
        "心存侥幸，先转2000元应急":
            jump ch14_C2
        "输入密码，转出全部2万":
            jump ch14_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch14_C1:
    scene bg_bedroom
    n "支付密码键盘弹出的那一刻，阿狐的手指停住了。"
    think serious "等等！老师的反诈课讲过AI换脸：视频能造假，声音能仿冒！爸爸出事绝不会瞒着妈妈，更不会让小学生转2万！"
    mc serious "这钱我不转。你要真是我爸，接我回拨的电话！"
    n "阿狐果断锁屏，拨打爸爸手机——爸爸正在开会，平安无事！"
    n "他又马上联系妈妈，一家人报警并提交了通话证据，反诈中心很快发布了预警。"
    dad laugh "儿子，你今天守住了全家最重要的防线，爸爸为你骄傲！"

    scene bg_living
    police serious "面对「以假乱真」的视频还能悬崖勒马，了不起！AI换脸再逼真，也怕「挂断回拨」这一招。涉及转账，先核实身份，再谈其他！"

    $ clear_chapter(14, 3)
    $ quick_menu = False
    call screen level_clear(14, 3, l14_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch14_C2:
    scene bg_bedroom
    n "阿狐想不出支付密码，便先用自己手机里的零花钱转了2000元「应急」。"
    think laugh "先把救命钱转过去，剩下的等妈妈回来再说。"
    n "2000元刚转走，「爸爸」立刻发来消息：怎么才转2000？快用你妈手机补上1万8，晚了对方就报警了！"
    mc confused "说好的救急，怎么比骗子催得还紧？"
    n "这时真爸爸来了电话，说自己正在开会、一切安好。阿狐如梦初醒，和妈妈一起报警，但2000元已被转走。"

    scene bg_living
    police serious "「先转一部分」也是上当！AI骗局里，骗子要的不是应急，而是你的全部。被骗的第一时间就该挂断核实，而不是替骗子「凑钱」！"

    $ clear_chapter(14, 1)
    $ quick_menu = False
    call screen level_clear(14, 1, l14_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch14_C3:
    scene bg_bedroom
    n "阿狐记住了妈妈输密码时的动作，试着拼了几次，竟然输对了支付密码。"
    n "2万元分两笔转了出去。转账成功，屏幕里的「爸爸」立刻挂断了电话，再拨过去已是关机。"
    n "十分钟后，真爸爸来电说自己正在开会。阿狐拿着手机，手都在发抖。"
    mc sad "爸……刚才是骗子冒充你，把妈妈卡里的2万块转走了……都怪我……"
    n "妈妈回家后没有责备他，第一时间报警、冻结银行卡。可大部分钱，已被骗子层层转移。"
    mom normal "钱是身外之物，你平安最重要。从今晚起，我们全家约定一个安全暗号，专门用来核实这种电话。"

    scene bg_bedroom
    police serious "小朋友记住！AI换脸能偷走爸爸的脸和声音，但偷不走「挂断回拨」和「家庭暗号」。视频谈钱必核实，支付密码是底线，守住了，骗局就破产！"

    $ quick_menu = False
    call screen level_fail(14, l14_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch14
    else:
        jump select_level
