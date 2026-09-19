# game/ch03.rpy
#
# 关卡3：冒充同学诈骗（盗号 / 高仿号冒充同学借钱垫付）
#
# 本关专属角色：骗子盗号后冒充的好朋友「小兔」。
# 小兔已有独立表情立绘（rabbit_*.png，script.rpy 已注册）。
define rabbit = Character("小兔", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="rabbit")

define l3_tip = "网友开口要转账，先打电话当面核，不垫付不扫码，验证码密码不给TA！"


label ch3:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周六的晚上，作业早就写完，阿狐窝在卧室里用平板和同学聊天。"
    n "班级群里，「小兔」的头像亮了起来——昵称、头像都和同桌小兔一模一样。"
    think normal "小兔周末也上线了，正好聊聊下周的班会。"
    rabbit laugh "阿狐！可算找到你了！我遇到急事了，你一定要帮帮我！"
    think confused "咦？小兔平时说话不是这个口气呀……可能她真的急坏了。"

    # === 第一轮抉择 ===
    rabbit laugh "我们课外班的老师说我弄坏了教室的投影仪，让我赔800块，不然就要告诉我爸妈！"
    rabbit laugh "我不敢跟家里人开口，你先借我800，我周一到学校就还你现金！求你了！"

    menu:
        "觉得口气有点怪，回复追问细节":
            jump ch3_B
        "好朋友有难，立刻答应帮忙垫付":
            jump ch3_C
        "网上不谈钱，先打电话向小兔本人核实":
            jump ch3_A


# ============ 分支A：理智避险 · 满分通关 ============
label ch3_A:
    scene bg_bedroom
    n "阿狐盯着屏幕，越看越觉得不对劲。"
    think serious "学校反诈班会讲过「冒充同学借钱」的骗局——真同学遇到了急事，打电话一问就知道！"
    n "阿狐的脑海里，响起了班主任猫头鹰老师在反诈班会上的声音。"
    teacher serious "同学们记住：账号会被盗、头像会造假。凡是「同学」在网上开口借钱，先挂断，打电话当面核实！"
    mc serious "借钱的事，网上说不好，我先打电话核实一下。"
    n "阿狐拨通了小兔的电话。小兔说自己的账号上周就被盗了，根本没发过赔投影仪的消息，课外班老师也从没罚过款。"
    n "阿狐立刻把聊天记录截图发给小兔妈妈，提醒小兔赶紧找回账号。"

    scene bg_living
    police laugh "太棒了！骗子盗取或高仿同学账号冒充本人借钱，是中小学生最容易上当的骗局之一。记住：凡是网上开口要钱的「同学」，一律先打电话、当面核实！"

    $ clear_chapter(3, 3)
    $ quick_menu = False
    call screen level_clear(3, 3, l3_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch3_B:
    scene bg_bedroom
    n "阿狐心里犯起了嘀咕，回复追问细节。"
    mc confused "你不是好好的吗？到底出了什么事？要赔800块钱？"
    rabbit worried "我手机被老师没收了，这是借同学账号上的聊天软件，你可千万别声张！"
    rabbit serious "老师催得紧，今天不赔就要告诉我爸妈。你先用你妈妈的手机扫这个码，把800转过去，我周一一定带现金还你！谢谢你，你是我最好的朋友！"
    n "对方发来一张收款码截图，收款人却是一个陌生的名字。"
    think confused "收款码上的名字，怎么既不是老师，也不是学校……"

    menu:
        "坚持要和小兔视频通话，见不到人不转钱":
            jump ch3_B2
        "拿着平板去客厅找妈妈核实":
            jump ch3_B1
        "有收款码应该错不了，按对方说的操作":
            jump ch3_B3


# B1：求助家长 · 满分
label ch3_B1:
    scene bg_living
    n "阿狐压住心里的着急，直接退出聊天，拿着平板走到客厅找妈妈。"
    think worried "虽然很想帮小兔，但网上借钱总觉得不太对劲，还是先问问妈妈吧。"
    n "老师班会上的叮嘱，也在耳边响了起来。"
    teacher serious "遇到网上借钱，自己拿不准的，不要回复、不要操作，第一时间告诉爸爸妈妈！"
    mc worried "妈妈，小兔在聊天软件上找我借800块钱赔老师的东西，你看是真的吗？"
    mom serious "宝贝，这是典型的「盗号冒充同学」骗局哦。你看这个收款码，收款人根本不是学校，名字还是个陌生人。真同学借钱不怕打电话核实，越是让你「保密、快转」的越可疑。"
    n "妈妈帮阿狐拨打小兔的电话核实——果然，小兔的账号被盗了，学校也从没罚过款。"

    scene bg_bedroom
    police laugh "求助家长做对了！遇到网上借钱，先停一停、问一问，和家长一起核实，骗子立刻现出原形！"

    $ clear_chapter(3, 3)
    $ quick_menu = False
    call screen level_clear(3, 3, l3_tip)
    $ quick_menu = True
    jump select_level


# B2：坚持视频核实 · 及时止损（2星）
label ch3_B2:
    scene bg_bedroom
    mc serious "转钱之前，我们先开个视频，我看看你本人再说。"
    rabbit worried "视频……不行不行！我手机被没收了，借来的手机摄像头是坏的，信号也不好，你别磨蹭了！"
    think serious "手机被没收、摄像头坏了、还一直催……小兔从来不会这样说话。这是骗子！"
    mc serious "我不转了。你要真是小兔，明天到学校当面跟我说。"
    n "对方立刻发来一连串催促的消息，见阿狐不再回复，头像很快变灰——账号显示已注销。"

    scene bg_living
    police serious "视频核实是识破冒充骗局的法宝！骗子最怕「见真人」，一要求视频就找各种借口推脱的，十有八九是骗子。"

    $ clear_chapter(3, 2)
    $ quick_menu = False
    call screen level_clear(3, 2, l3_tip)
    $ quick_menu = True
    jump select_level


# B3：轻信收款码 · 轻微泄露（1星）
label ch3_B3:
    scene bg_bedroom
    n "阿狐觉得对方连收款码都发来了，应该不会是假的，便打开妈妈的手机准备扫码。"
    n "刚扫完码，妈妈的手机就收到一条短信验证码，对方紧接着发来消息。"
    rabbit laugh "快！把刚收到的6位数字发给我，系统要验证一下，发完钱就转过去了！"
    n "阿狐正要把数字念出来，突然想起老师的反诈课堂：验证码就是钱，谁要都不能给！"
    think serious "等等！老师说过，验证码谁要都不能给！"
    mc serious "我不发了，你是骗子！"
    n "阿狐立刻停止操作，把平板拿给妈妈。妈妈当场修改支付密码、冻结付款渠道，没有造成损失。"

    scene bg_living
    police serious "好险！验证码和支付密码就是钱包的钥匙，任何索要验证码的「同学」「老师」「客服」都是骗子。你能及时刹住车，守住了妈妈的钱包！"

    $ clear_chapter(3, 1)
    $ quick_menu = False
    call screen level_clear(3, 1, l3_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch3_C:
    scene bg_bedroom
    n "阿狐一心想着帮好朋友，没有丝毫犹豫。"
    think laugh "小兔是我的好朋友，她这么着急，我一定要帮她！"
    mc laugh "别怕别怕，我这就帮你转，你等我！"
    rabbit laugh "太好了！你真是我的救命恩人！快用你妈妈的手机扫码转800，动作快点，老师马上就要告诉我爸妈了！"
    n "对方又发来一段带着哭腔的语音，一遍遍催促阿狐快点转账。"

    menu:
        "转账前猛然醒悟，先核实再说":
            jump ch3_C1
        "心存侥幸，先少转100试试真假":
            jump ch3_C2
        "按对方要求，立刻扫码转账800":
            jump ch3_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch3_C1:
    scene bg_bedroom
    n "手指停在付款按钮上方，阿狐心里突然咯噔一下。"
    think serious "不对！小兔就住我家隔壁，真出了这么大的事，她妈妈肯定直接来找我妈，怎么会只在聊天软件上找我借钱？学校反诈班会讲过——网上开口要钱的「同学」，多半是盗号的骗子！"
    mc serious "钱我不能转。你要真是小兔，就和我视频，或者我打电话给你妈妈核实。"
    n "对面瞬间没了声音。阿狐把聊天记录拿给妈妈看，妈妈联系小兔妈妈一核实——小兔的账号被盗了，根本没有赔投影仪这回事。"

    scene bg_living
    mom laugh "你能在「帮朋友」的大事面前冷静核实，做得太棒了！"
    police serious "临「钱」不乱，先核实再决定，这就是反诈的高手！记住：网友、同学网上借钱，一律电话、当面核实后再说。"

    $ clear_chapter(3, 3)
    $ quick_menu = False
    call screen level_clear(3, 3, l3_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch3_C2:
    scene bg_bedroom
    n "阿狐既怕错过帮朋友的时机，又有点不放心，决定先少转一点试试真假。"
    think laugh "先转100，万一是骗子也亏得少；真是小兔，再转剩下的也不迟。"
    n "阿狐用妈妈的手机扫码，转出了100元。"
    n "钱刚转过去，对方的消息就轰炸了过来。"
    rabbit serious "怎么才转100？快把剩下的700转了！不然老师马上就告诉我爸妈了！"
    mc confused "咦？说好我垫付、周一还现金，怎么一直催着我转剩下的……"
    n "阿狐越想越不对，把事情告诉了妈妈。妈妈联系小兔妈妈核实——小兔账号被盗，那100元已经追不回来了。"

    scene bg_living
    mc sad "唉，我不该抱着侥幸心理先转钱的……"
    police serious "骗子的套路就是一步步试探你的底线！只要转出第一笔钱，骗子就会得寸进尺。网上借钱不核实，一分钱都不能转！"

    $ clear_chapter(3, 1)
    $ quick_menu = False
    call screen level_clear(3, 1, l3_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch3_C3:
    scene bg_bedroom
    n "阿狐深信不疑，用妈妈的手机扫码，输入800元，点击付款。"
    n "转账成功。对方发来一个笑脸，紧接着又发来消息。"
    rabbit laugh "太谢谢啦！老师又说还要交200元修理费，你再转200，凑够1000就彻底没事啦！"
    n "阿狐心里犯起嘀咕，赶紧拿着手机去客厅找妈妈。妈妈打开账单一看——800元早已被转走。"
    n "再点开聊天框，发出去的消息带着红色感叹号：对方已将阿狐拉黑，「小兔」的账号也显示已注销。"

    scene bg_living
    mc sad "我……我被骗了……那是妈妈的血汗钱……"
    n "阿狐哭着向妈妈承认了错误，妈妈抱了抱他。"
    mom normal "没关系，钱的事情以后一定要先告诉我们。记住：网上开口要钱的「同学」，先打电话核实；转账之前，永远先问爸爸妈妈。"

    scene bg_bedroom
    police serious "小朋友一定要记住！盗号冒充熟人借钱，是针对中小学生最常见的诈骗。凡是涉及转账，一定要：一核实（电话、当面）、二报告（家长老师）、三拒绝（陌生收款码）。贪一时「讲义气」，损失的可能是全家的血汗钱！"

    $ quick_menu = False
    call screen level_fail(3, l3_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch3
    else:
        jump select_level
