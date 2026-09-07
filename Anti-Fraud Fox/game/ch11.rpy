# game/ch11.rpy
#
# 关卡11：刷单垫资诈骗（点赞兼职 + 大额垫付任务）

define l11_tip = "刷单兼职是陷阱，先给甜头后收割，垫资任务别去碰，踏实省钱最安心！"


label ch11:

    # === 前置剧情 ===
    scene bg_bedroom
    n "暑假第一天，阿狐盯上了商店里那台新款游戏机，可惜零花钱还差一大截。"
    n "刷短视频时，一条广告跳了出来：「动动手指，日赚100！学生党在家兼职，点赞关注就赚钱！」"
    mc laugh "点赞就能赚钱？那我的游戏机有希望了！"
    n "阿狐按照广告加了「兼职客服」。"
    fraud laugh "欢迎加入！任务超简单：给指定视频点赞、关注，一单5元，日结工资，多劳多得！"

    # === 第一轮抉择 ===
    fraud serious "兼职名额有限，今天报名今天上岗，先做一单试试水！"

    menu:
        "想起老师的告诫：刷单都是骗局，退出去":
            jump ch11_A
        "问一问：点赞这种事，为什么给钱？":
            jump ch11_B
        "主动完成任务，等着领第一笔工资":
            jump ch11_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch11_A:
    scene bg_bedroom
    n "阿狐盯着「日赚100」的广告，忽然想起老师的告诫。"
    think serious "老师说，刷单本身就是违法行为，还十有八九是骗局——真有这么容易赚钱，谁还去上班呀？"
    mc serious "点赞刷单赚钱不可信，我不做！"
    n "阿狐举报了广告和账号，还提醒同桌别上当。"
    n "几天后，同桌说班里有同学做这个「兼职」，垫进去两百多块全没了。"

    scene bg_living
    police laugh "清醒！「刷单兼职」是明令禁止的违法行为，更是诈骗重灾区。记住：动动手指就日赚百元的好事，都是冲着你的本金来的！"

    $ clear_chapter(11, 3)
    $ quick_menu = False
    call screen level_clear(11, 3, l11_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch11_B:
    scene bg_bedroom
    mc confused "不就是点个赞吗？你们为什么要花钱请人点赞呀？"
    fraud laugh "商家搞活动需要人气嘛！平台拨款给我们做推广，工资自然由我们发，你只管赚！"
    n "对方发来一沓「员工工资结算截图」，红彤彤的转账记录看着很诱人。"
    fraud serious "简单任务赚钱少，想赚大钱就做「高级任务」：下载我们的接单APP，垫付刷大单，佣金翻十倍！"

    menu:
        "拿不准，先把APP的事告诉妈妈":
            jump ch11_B1
        "赚到5元后觉得不对，果断收手":
            jump ch11_B2
        "下载APP，抢一个「高级任务」":
            jump ch11_B3


# B1：求助家长 · 满分
label ch11_B1:
    scene bg_living
    n "阿狐退出对话，拿着手机找妈妈。"
    think worried "前几单真给钱了呀……可「垫付大单」听着有点吓人，还是问问妈妈。"
    mc worried "妈妈，有个兼职先给我5块钱让我点赞，现在让我下载APP垫付刷大单，说佣金翻十倍，是真的吗？"
    mom serious "宝贝，这是「刷单诈骗」！先给甜头是鱼饵，垫付大单才是收割。你看那些「工资截图」，全是软件做出来的假图。刷单本来就违法，赶紧远离。"
    n "妈妈陪阿狐举报了广告和账号，还给他讲了邻居家孩子刷单被骗上万元的新闻。"

    scene bg_bedroom
    police laugh "问得及时！刷单诈骗的铁律：小单返利是诱饵，大单垫资是收割。凡是让你先垫钱的「兼职」，一律是诈骗！"

    $ clear_chapter(11, 3)
    $ quick_menu = False
    call screen level_clear(11, 3, l11_tip)
    $ quick_menu = True
    jump select_level


# B2：拿钱收手 · 及时止损（2星）
label ch11_B2:
    scene bg_bedroom
    n "阿狐做了两单点赞任务，真收到了10元工资。"
    n "对方随即发来「高级任务」邀请，阿狐却越想越不对。"
    think serious "为什么给我钱这么痛快，一到「垫付大单」就又是APP又是佣金翻倍？天上掉馅饼，八成是陷阱！"
    mc serious "高级任务我不做了，谢谢。"
    n "阿狐收手退群。一周后，群里另一个「兼职学生」按同样的话术垫了2000元，再也没能提现。"

    scene bg_living
    police serious "拿小钱、停大坑，止损及时！记住：骗子先让你赚5元，是为了后面骗你5000元。见好就收，是聪明，更是清醒！"

    $ clear_chapter(11, 2)
    $ quick_menu = False
    call screen level_clear(11, 2, l11_tip)
    $ quick_menu = True
    jump select_level


# B3：下载APP做高级任务 · 轻微受害（1星）
label ch11_B3:
    scene bg_bedroom
    n "阿狐下载了「接单APP」，抢到一个高级任务：垫付100元下单，10分钟后返还本金加30元佣金。"
    n "他垫付了100元。几分钟后，页面显示「任务完成，佣金100元+本金待结算」，可提现按钮却一直转圈。"
    fraud serious "系统提示：需连续完成3单才能合并提现，当前进度1/3。放弃任务，已垫资金不予退还哦！"
    think serious "等等！钱进去就出不来了，这是连环套！"
    mc serious "我不做了，把我的100元退回来！"
    n "客服不再理会。阿狐把事情告诉妈妈，妈妈立刻报警备案，但那100元早已无法追回。"

    scene bg_living
    police serious "「连续做单才能提现」就是刷单诈骗的核心套路！100元买个教训：刷单兼职碰不得，垫付资金有去无回！"

    $ clear_chapter(11, 1)
    $ quick_menu = False
    call screen level_clear(11, 1, l11_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch11_C:
    scene bg_bedroom
    n "阿狐认真完成了两单点赞任务，真的收到了10元工资。"
    think laugh "躺着赚钱是真的！我得抓紧做高级任务，游戏机指日可待！"
    mc laugh "客服你好，高级任务在哪接？我要赚大钱！"
    fraud laugh "好眼光！当前最火的是「三联单」：连续垫付三笔共2000元，任务完成返还本金2600元，赚600元！"

    menu:
        "转账前猛然醒悟，退出APP":
            jump ch11_C1
        "心存侥幸，先垫第一笔500元":
            jump ch11_C2
        "为了600元佣金，垫付全部2000元":
            jump ch11_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch11_C1:
    scene bg_bedroom
    n "手指悬在转账按钮上方，阿狐心里突然咯噔一下。"
    think serious "等等！我刚才赚的10元，是不是就是为了让我相信「大单」的鱼饵？老师说，先给甜头后收割，就是刷单诈骗！"
    mc serious "大单我不做了。你们这种先给小钱、再骗大钱的套路，我见识过了！"
    n "阿狐卸载APP、举报账号，把完整经过告诉妈妈。妈妈夸奖了他，还把案例分享到了家长群。"

    scene bg_living
    police serious "能从小甜头里看出大陷阱，这就是反诈的火眼金睛！记住：刷单返利是诱饵，垫资大单是收割，一步都不要踏进去！"

    $ clear_chapter(11, 3)
    $ quick_menu = False
    call screen level_clear(11, 3, l11_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch11_C2:
    scene bg_bedroom
    n "阿狐决定先垫第一笔500元「试试水」。"
    think laugh "先垫500，万一真是真的呢？不合适我就停。"
    n "500元转过去，页面立刻弹出：三联单任务绑定账户，中途退出视为违约，已垫资金全部没收。"
    fraud serious "你已违约！按平台规则需再缴1000元违约金解冻，否则账户永久冻结并上报征信！"
    mc confused "怎么一转钱规则全变了……"
    n "阿狐把事情告诉妈妈，妈妈立刻报警。500元垫付款和「解冻违约金」，一分都没能追回。"

    scene bg_living
    police serious "骗子的话术永远「差一单」「差一步」，目的只有一个：让你不停转钱。记住：刷单垫资，进去了就别想全身而退！"

    $ clear_chapter(11, 1)
    $ quick_menu = False
    call screen level_clear(11, 1, l11_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch11_C3:
    scene bg_bedroom
    n "阿狐把攒了半年的2000元压岁钱全部垫付进去，满心等着返还2600元。"
    n "第一笔、第二笔都顺利「结算」，第三笔刚转完，页面却弹出：操作超时，订单冻结，需再充值5000元才能全部提现。"
    n "阿狐慌了，找「客服」理论，客服却让他「先交钱再谈退款」。"
    n "再发消息，APP账号已被封禁，客服销号失联。2000元压岁钱，一分没回来。"
    mc sad "我的压岁钱……还说要赚600的，怎么全赔进去了……"
    n "阿狐哭着向妈妈坦白，妈妈立刻报警。"
    mom normal "压岁钱没了可以再攒，教训必须记住：想赚快钱的念头一起，骗子的钩子就到嘴边了。"

    scene bg_bedroom
    police serious "小朋友记住！刷单诈骗三部曲：小利诱惑、任务加码、垫资收割。所有让你垫钱的「兼职」都是诈骗，踏实学习、合理攒钱，才是真正的「日赚100」！"

    $ quick_menu = False
    call screen level_fail(11, l11_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch11
    else:
        jump select_level
