# game/ch07.rpy
#
# 关卡7：租号卖号诈骗（高价收号 + 解冻金骗局）

define l7_tip = "账号密码是财产，租号卖号风险大，解冻保证金是谎言，官方渠道才可靠！"


label ch7:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周日中午，阿狐的游戏账号好不容易练到了高级段位，皮肤和道具攒了一大堆。"
    n "游戏交流群里，一条消息弹了出来。"
    fraud laugh "高价收游戏账号！高级号500元起收，租号每月150元！走「官方担保平台」，安全无忧，童叟无欺！"
    think laugh "我的账号能卖500？那新游戏机不就有盼头了！"

    # === 第一轮抉择 ===
    fraud laugh "有意向加我，发账号评估价格，三分钟出结果！"

    menu:
        "问一问：担保平台交易具体怎么操作？":
            jump ch7_B
        "想起账号是重要财产，不理会并举报":
            jump ch7_A
        "主动发账号，让「客服」评估高价":
            jump ch7_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch7_A:
    scene bg_bedroom
    n "阿狐盯着「500元收号」的消息，心里犯起了嘀咕。"
    think serious "账号是我练了好几年的心血，也是爸爸妈妈花钱养的。老师说，虚拟财产同样重要，不能交给陌生人！"
    mc serious "租号卖号风险太大了，账号被盗、被拿去干坏事，责任都是我的。我不卖！"
    n "阿狐退出了群聊，还截图举报了这条收号广告。"

    scene bg_living
    police laugh "好样的！游戏账号绑着手机号、支付方式，卖号租号等于把「家门钥匙」交给别人。骗子还常用租来的账号实施诈骗、洗钱，账号主人也要担责任！"

    $ clear_chapter(7, 3)
    $ quick_menu = False
    call screen level_clear(7, 3, l7_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch7_B:
    scene bg_bedroom
    mc confused "担保平台交易，具体是怎么个担保法呀？"
    fraud laugh "很简单！点击我发的「平台链接」，把账号密码填进去评估，平台显示价格后你确认出售，钱立刻到账，平台全程担保！"
    n "对方发来一个和正规交易平台长得几乎一样的链接。"
    fraud serious "评估要趁早，高价号源马上满了，晚一步价格就掉啦！"

    menu:
        "坚持只在官方平台交易，拒绝陌生链接":
            jump ch7_B2
        "点开链接，按提示填写账号密码":
            jump ch7_B3
        "退出对话，把链接拿给爸爸看":
            jump ch7_B1


# B1：求助家长 · 满分
label ch7_B1:
    scene bg_living
    n "阿狐关掉对话，拿着手机找到爸爸。"
    think worried "平台看起来挺正规的，可「填账号密码」这一步，总觉得不太对劲。"
    mc worried "爸爸，有人说我的游戏账号值500元，让我在链接里填账号密码评估，是真的吗？"
    dad serious "儿子，这是「收号」骗局！你看这个链接，域名和官方平台差了两个字母，是高仿钓鱼网站。账号密码一填，号瞬间就被盗走。"
    n "爸爸陪阿狐举报了链接，还帮账号开启了更高级的安全验证。"

    scene bg_bedroom
    police laugh "问家长问得好！游戏账号密码等于账号的「全部钥匙」，任何索要密码的「平台」「客服」，一律是骗子！"

    $ clear_chapter(7, 3)
    $ quick_menu = False
    call screen level_clear(7, 3, l7_tip)
    $ quick_menu = True
    jump select_level


# B2：坚持官方渠道 · 及时止损（2星）
label ch7_B2:
    scene bg_bedroom
    mc serious "交易我只走官方平台，陌生链接我一律不点。你要真想收号，就到官方平台挂单。"
    fraud serious "官方平台手续费太高了！链接是内部通道，不点就别怪我没提醒你，高价名额马上没了！"
    think serious "真平台不怕走官方流程，怕的一定是骗子。"
    n "阿狐不再理会。当晚，群里另一名同学按同款链接填了账号密码，高级号连同所有皮肤瞬间被盗，追悔莫及。"

    scene bg_living
    police serious "你的坚持救了自己！记住：所有「绕开官方」的私下交易链接，都是钓鱼网站。宁可少卖点钱，也绝不交出密码！"

    $ clear_chapter(7, 2)
    $ quick_menu = False
    call screen level_clear(7, 2, l7_tip)
    $ quick_menu = True
    jump select_level


# B3：填写账号密码 · 轻微泄露（1星）
label ch7_B3:
    scene bg_bedroom
    n "阿狐点开链接，看着逼真的平台页面，填入了游戏账号和密码。"
    n "页面随即显示：账号已锁定，需缴纳50元「解冻保证金」完成评估，解冻后原路退回。"
    fraud serious "快付保证金，不然账号会被平台冻结三天，影响信誉哦！"
    think serious "等等！评估账号怎么还要交保证金？老师说过，这是「解冻金」骗局的套路！"
    mc serious "我不付了，你们是钓鱼平台！"
    n "阿狐立刻退出页面，把事情告诉爸爸。爸爸马上修改了游戏密码、解绑了关联支付，账号保住了。"

    scene bg_living
    police serious "好险！密码已经泄露，好在改得及时。「解冻金」「保证金」是收号骗局的第一刀，再往下就是连环收费。账号密码，永远不给陌生人！"

    $ clear_chapter(7, 1)
    $ quick_menu = False
    call screen level_clear(7, 1, l7_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch7_C:
    scene bg_bedroom
    n "阿狐一心想卖个好价钱，把账号密码填进了对方发来的「平台链接」。"
    think laugh "高级号，怎么也得值个500块吧！"
    mc laugh "我的账号是高级号，皮肤很多，你快评估一下！"
    fraud laugh "评估完毕：你的账号价值520元！钱已打入平台账户，请登录「平台」提现。"
    n "阿狐登录链接页面，却弹出提示：账户异常冻结，需缴纳500元「解冻金」才能提现，否则将扣除1000元违约金。"
    fraud serious "这是平台规定！不交解冻金，还要赔偿违约金，账号也会被没收！"

    menu:
        "心存侥幸，先交100元「小额解冻」试试":
            jump ch7_C2
        "猛然醒悟，识破「解冻金」骗局":
            jump ch7_C1
        "怕赔违约金，赶紧交500元解冻金":
            jump ch7_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch7_C1:
    scene bg_bedroom
    n "看着「再交500」的要求，阿狐心里突然咯噔一下。"
    think serious "不对！明明是我卖号收钱，怎么反而要我不停交钱？老师说过，「解冻金」「保证金」全是收号骗局的套路！"
    mc serious "我不交！你们这是钓鱼平台，我要举报你，还要把链接交给警察叔叔！"
    n "阿狐退出页面，把整件事告诉爸爸。爸爸马上修改游戏密码、开启登录保护，并向平台官方举报了钓鱼链接。"
    dad laugh "临「钱」不乱，还知道保留证据，儿子真棒！"

    scene bg_living
    police serious "识破「卖号反被收钱」的把戏，反应很快！记住：凡是让你交钱才能「提现」「解冻」的，都是骗局，交得越多陷得越深！"

    $ clear_chapter(7, 3)
    $ quick_menu = False
    call screen level_clear(7, 3, l7_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch7_C2:
    scene bg_bedroom
    n "阿狐舍不得「账户里」的520元，决定先交100元「小额解冻费」试试。"
    think laugh "先交100，账号解冻了，520元不就回来了？"
    n "100元转过去，页面又提示：解冻进度30%%，需再交400元完成全部解冻。"
    mc confused "怎么解冻还有进度条？这钱到底还提不提得出来？"
    n "阿狐把事情告诉爸爸。爸爸说这就是连环骗局，之前的钱都打了水漂，好在账号密码马上改掉，没被一锅端。"

    scene bg_living
    police serious "骗子的「解冻进度」永远差最后一截！止损最好的时机，就是识破骗局的那一刻。多交的100元，买了个教训。"

    $ clear_chapter(7, 1)
    $ quick_menu = False
    call screen level_clear(7, 1, l7_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch7_C3:
    scene bg_bedroom
    n "阿狐害怕赔1000元违约金，把攒的500元零花钱全部交了「解冻金」。"
    n "页面却再次弹出：检测到未成年人操作，需再交800元「实名认证金」，否则账户永久冻结、违约金翻倍。"
    n "与此同时，阿狐发现自己的游戏账号已在别处登录——密码被骗子改了，高级号、皮肤、道具全部易主。"
    mc sad "号没了，钱也没了……我怎么办呀……"
    n "阿狐哭着向爸爸坦白。爸爸第一时间联系游戏官方申诉冻结账号，并报了警。"
    dad normal "吃一堑长一智。账号和钱的事，以后一定先跟爸爸妈妈商量。"

    scene bg_bedroom
    police serious "小朋友记住！「高价收号」骗局两步走：钓鱼链接骗走账号，解冻金骗走存款。账号密码不外传，私下交易不参与，官方渠道才可靠！"

    $ quick_menu = False
    call screen level_fail(7, l7_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch7
    else:
        jump select_level
