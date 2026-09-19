# game/ch10.rpy
#
# 关卡10：私密照勒索诈骗（网上「好友」索照后威胁）
#
# 本关专属角色：骗子冒充的游戏网友「小雨」（复用诈骗犯浣熊的立绘）。
define xiaoyu = Character("小雨", who_color="#ffffff", who_outlines=[(2, "#000000", 0, 0)], image="fraud")

define l10_tip = "身体隐私不拍摄，私密照片不外发，遇到威胁不害怕，第一时间告诉爸妈！"


label ch10:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周六下午，阿狐在游戏里认识了一位「同班玩家」，对方昵称「小雨」，说自己也是小学生，玩同一款游戏。"
    n "几天聊下来，两人组队越来越默契，「小雨」还主动分享了动画、聊学校趣事，阿狐把她当成了好朋友。"
    xiaoyu laugh "阿狐，我们互换一张照片吧，看看对方长什么样呀！我先发我的，你也要发哦！"
    n "对方发来一张小女孩的照片，看起来活泼可爱。"
    think normal "聊了这么久，交换张照片也正常吧……"

    # === 第一轮抉择 ===
    xiaoyu laugh "照片太模糊啦！你发一张穿着睡衣、光着膀子的照片，我们才是真正的好朋友嘛，我都发过了，你怕什么呀！"

    menu:
        "觉得别扭，回复问她为什么要这种照片":
            jump ch10_B
        "怕朋友生气，按她说的拍了照片":
            jump ch10_C
        "感觉不对劲，拒绝要求并拉黑举报":
            jump ch10_A


# ============ 分支A：理智避险 · 满分通关 ============
label ch10_A:
    scene bg_bedroom
    n "「光膀子的照片」这个要求让阿狐心里咯噔一下。"
    think serious "老师讲过：身体的隐私部位不能给任何人看、不能拍照，网上「朋友」要这种照片，绝对不正常！"
    mc serious "这种照片我不能发，谁要都不能发！"
    n "阿狐立刻退出游戏，把聊天记录截图给妈妈看。妈妈表扬了他，陪他举报拉黑了账号，并向游戏平台申诉。"
    mom serious "宝贝，这种「套照片」的账号背后往往是成年人骗子！你做得完全正确，隐私照片一张都不能发！"

    scene bg_living
    police laugh "警惕性满分！索要私密照片的都是坏人，不管他说得多好听、是不是「同龄人」。不发、不拍、马上告诉家长，你就是最安全的孩子！"

    $ clear_chapter(10, 3)
    $ quick_menu = False
    call screen level_clear(10, 3, l10_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：犹豫追问 · 进入第二轮 ============
label ch10_B:
    scene bg_bedroom
    mc confused "为什么要这种照片呀？普通合照不行吗？"
    xiaoyu serious "你不发就是不喜欢我这个朋友！班里的同学都互相发过，就你磨磨唧唧的。"
    xiaoyu laugh "快发一张，发完我把我珍藏的皮肤账号送你玩！"
    n "对方一边用「友情」绑架，一边用「游戏账号」做诱饵，不断催促。"

    menu:
        "拿不准，退出游戏找妈妈商量":
            jump ch10_B1
        "坚决拒绝，删好友退出游戏":
            jump ch10_B2
        "不好意思拒绝，发了张普通生活照":
            jump ch10_B3


# B1：求助家长 · 满分
label ch10_B1:
    scene bg_living
    n "阿狐退出游戏，拿着平板走到客厅找妈妈。"
    think worried "她平时聊得挺好的，可这个要求太奇怪了……还是先问问妈妈。"
    mc worried "妈妈，游戏里认识的「同学」让我发穿睡衣的照片，还说不发就不是好朋友，我该怎么办？"
    mom serious "宝贝，这是「套私密照」的骗局！真正的朋友不会用绝交逼你拍隐私照片。这类照片一旦发出去，就可能被坏人拿去威胁你。你不发，就是最对的！"
    n "妈妈陪阿狐举报拉黑了账号，并把游戏的好友申请设置成了「仅限现实好友」。"

    scene bg_bedroom
    police laugh "做得棒！用「绝交」「礼物」逼你发隐私照片的，不管是谁，都是坏人。守住底线，马上告诉家长，你做得非常好！"

    $ clear_chapter(10, 3)
    $ quick_menu = False
    call screen level_clear(10, 3, l10_tip)
    $ quick_menu = True
    jump select_level


# B2：坚决拒绝 · 及时止损（2星）
label ch10_B2:
    scene bg_bedroom
    mc serious "这种照片我绝不发。你不是我朋友，朋友不会逼我做这种事！"
    xiaoyu serious "行啊你！等着，我有的是办法让你后悔！"
    n "阿狐没有被吓住，果断删除好友、退出游戏。当晚他把这件事告诉了妈妈，妈妈帮他检查了账号隐私设置，并肯定了他的做法。"

    scene bg_living
    police serious "拒绝得干脆，做得对！不过下次记住：遇到这种骚扰，第一时间告诉家长和老师，让大人帮你处理，比你一个人硬扛更稳妥。"

    $ clear_chapter(10, 2)
    $ quick_menu = False
    call screen level_clear(10, 2, l10_tip)
    $ quick_menu = True
    jump select_level


# B3：发普通照片 · 轻微泄露（1星）
label ch10_B3:
    scene bg_bedroom
    n "阿狐不好意思拒绝，发了一张穿校服的普通生活照过去。"
    n "对方却立刻变本加厉：要求拍更私密的部位，「不拍就把照片发给全校同学，说你是个坏孩子」。"
    xiaoyu serious "快点拍！不然你这张照片加上编好的「坏话」，马上出现在你们班级群里！"
    think serious "她开始威胁我了！老师说过的「套照片骗局」是真的！"
    mc serious "我不怕你！我要把聊天记录全部告诉老师和妈妈！"
    n "阿狐马上截图告诉了妈妈和班主任。老师上报学校并协助报警，骗子账号被封禁。"

    scene bg_living
    police serious "照片已经泄露，但你的处理非常正确：不害怕、不妥协、马上告诉大人！记住，被威胁时，老师和警察永远是你的后盾。"

    $ clear_chapter(10, 1)
    $ quick_menu = False
    call screen level_clear(10, 1, l10_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch10_C:
    scene bg_bedroom
    n "阿狐怕失去这个「好朋友」，真的拍了照片发了过去。"
    think laugh "她都先发我了，我应该讲义气……"
    xiaoyu laugh "乖~ 再拍一张更隐私的，我就把皮肤账号给你！"
    n "阿狐犹豫着又拍了一张。就在发送成功的下一秒，对方的头像和昵称突然全变了。"
    xiaoyu serious "小子，看清楚了吧？你刚才的照片都在我手里。给我转5000元，不然我把照片发到你们学校贴吧和班级群，让你没法做人！"

    menu:
        "用零花钱先转500元求对方删照片":
            jump ch10_C2
        "惊醒：不转钱，立刻告诉爸妈报警":
            jump ch10_C1
        "太害怕了，瞒着家长偷偷转账":
            jump ch10_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch10_C1:
    scene bg_bedroom
    n "阿狐吓得不轻，但他死死记住了一条底线。"
    think serious "老师说过：就算照片被坏人拿到，错的也是坏人，绝不能乖乖转钱！这种事第一时间告诉爸妈，永远不会错！"
    mc serious "照片你可以随便发，钱我一分不会给。我现在就把所有聊天记录交给警察！"
    n "阿狐立刻冲到客厅，把经过一五一十告诉妈妈。妈妈没有责备他，马上报警，并保留了全部聊天证据。"
    n "民警很快锁定了账号，骗子见阿狐家报了警，账号连夜注销，再也没敢出现。"
    mom laugh "你今天比大人还勇敢！记住：无论发生什么，爸妈永远是你的靠山。"

    scene bg_living
    police serious "处理堪称教科书！遇到「私密照勒索」：不转钱、不删证据、立刻报告家长和警察。记住：被威胁不是你的错，妥协才会让坏人得寸进尺！"

    $ clear_chapter(10, 3)
    $ quick_menu = False
    call screen level_clear(10, 3, l10_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸妥协 · 轻微受害（1星）
label ch10_C2:
    scene bg_bedroom
    n "阿狐把攒了一年的500元零花钱转了过去，求对方删照片。"
    think laugh "给了钱，他就应该把照片删了吧……"
    xiaoyu serious "500就想打发我？你父母是开公司的吧？再转3000，不然照片立刻发出！"
    mc confused "说好给钱就删照片的，怎么又要更多？"
    n "阿狐终于崩溃，哭着把一切告诉了妈妈。妈妈立刻报警——但转出去的500元，早被骗子转移了。"

    scene bg_living
    police serious "记住：给勒索者转钱，就像往无底洞里填土，永远不会填满。被骗照片威胁，唯一正确的做法就是：不转钱、留证据、报告家长和警察！"

    $ clear_chapter(10, 1)
    $ quick_menu = False
    call screen level_clear(10, 1, l10_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch10_C3:
    scene bg_bedroom
    n "阿狐太害怕了，不敢告诉任何人，把零花钱1000元全部转了过去。"
    n "对方收了钱，不但没删照片，反而变本加厉，隔三差五发消息威胁：「再转2000，不然全班都看到。」"
    n "阿狐吃不下饭、睡不着觉，成绩一落千丈，天天提心吊胆。一个月后，班主任发现他情绪异常，耐心询问下，他才哭着说出实情。"
    n "老师和家长立刻报警，骗子落网了——但已转走的1000元，只追回了一小部分。"
    mc sad "我应该一开始就告诉爸妈的……一个人扛，越扛越糟……"

    scene bg_living
    police serious "小朋友记住！私密照被勒索，瞒着大人是最大的错误。你越害怕、越妥协，坏人越嚣张。第一时间告诉爸妈和警察，天塌不下来，大人一定能帮你！"

    $ quick_menu = False
    call screen level_fail(10, l10_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch10
    else:
        jump select_level
