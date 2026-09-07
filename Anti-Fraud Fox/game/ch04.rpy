# game/ch04.rpy
#
# 关卡4：快递中奖诈骗（快递里的中奖刮刮卡）

define l4_tip = "陌生快递有猫腻，刮卡中奖是陷阱，领奖先要交钱的，统统都是骗子！"


label ch4:

    # === 前置剧情 ===
    scene bg_living
    n "周六上午，妈妈网购的快递到了，阿狐抢着帮忙拆箱。"
    n "拆开纸箱，生活用品下面居然躺着一张烫金卡片：「电商周年庆·幸运用户刮刮卡」，还印着电商标志。"
    mc laugh "妈妈快看，快递里还送了张刮刮卡！"
    n "阿狐用力一刮——「恭喜您中得二等奖：平板电脑一台，价值2999元！」"
    think laugh "哇，平板电脑！我们这是撞大运了吗？"
    n "卡片背面写着：扫码添加客服，验证身份即可领取奖品。"

    # === 第一轮抉择 ===
    scene bg_bedroom
    n "阿狐扫码加上了一个昵称叫「中奖客服」的人。"
    fraud laugh "恭喜恭喜！您中了我们周年庆的二等奖，平板电脑一台！只要缴纳200元「好运运费」，奖品立刻包邮到家！"
    fraud serious "名额有限，今天不领，奖品就回收作废了哦！"

    menu:
        "觉得不对劲，把刮刮卡拿给妈妈看":
            jump ch4_A
        "问清楚：为什么中奖了还要先交钱？":
            jump ch4_B
        "难得中奖，主动追问怎么领奖":
            jump ch4_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch4_A:
    scene bg_living
    n "阿狐盯着卡片上「先交钱」三个字，越想越不对：中奖是好事，为什么要我先掏钱？"
    think serious "学校反诈课讲过，正规中奖不会让中奖人先交钱！"
    mc serious "妈妈，快递里的刮刮卡说我中了平板，但要先交200元运费，是真的吗？"
    mom serious "宝贝，这是骗子塞进快递里的「中奖卡」！这种卡人人刮开都「中奖」，为的就是骗你扫码交钱。天上不会掉馅饼，直接扔掉。"
    n "妈妈把刮刮卡扔进垃圾桶，还提醒了快递驿站和邻居们注意。"

    scene bg_bedroom
    police laugh "做得好！「快递刮刮卡中奖」是骗子混进物流环节的老套路，卡片人人「中奖」，专门骗「运费」「保证金」。凡是领奖先交钱，一律是诈骗！"

    $ clear_chapter(4, 3)
    $ quick_menu = False
    call screen level_clear(4, 3, l4_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch4_B:
    scene bg_bedroom
    mc confused "不是说我中奖了吗？为什么领奖还要我先交钱呀？"
    fraud laugh "这是快递保价费和人工派送费呀，官方补贴了大部分，您只需承担200元！您看，昨天有位阿姨刚领走平板，这是签收图！"
    n "对方发来一张「用户签收」照片，看起来有模有样。"
    fraud serious "您只需提供姓名、电话、收货地址，再扫码付200元运费，平板今晚就发货！"

    menu:
        "关掉对话，拿着手机去问妈妈":
            jump ch4_B1
        "要求货到付款，收到平板再给钱":
            jump ch4_B2
        "按对方要求填写信息、准备付运费":
            jump ch4_B3


# B1：求助家长 · 满分
label ch4_B1:
    scene bg_living
    n "阿狐压住心里的期待，关掉对话，拿着手机走到客厅找妈妈。"
    think worried "虽然很想要平板，但中奖还要先交钱，总觉得不太对劲。"
    mc worried "妈妈，刮刮卡说我中了平板，客服却让我先交200元运费，你看是真的吗？"
    mom serious "假的宝贝。你看这张卡，随便谁刮开都「中大奖」；签收图是骗子伪造的。领奖先交钱的，百分之百是诈骗。"
    n "妈妈陪阿狐举报拉黑了对方，还把刮刮卡拍照发到业主群，提醒大家别上当。"

    scene bg_bedroom
    police laugh "遇到可疑的中奖先停一停、问家长，你们做得非常棒！记住：正规奖品从不需要中奖人先付费！"

    $ clear_chapter(4, 3)
    $ quick_menu = False
    call screen level_clear(4, 3, l4_tip)
    $ quick_menu = True
    jump select_level


# B2：要求货到付款 · 及时止损（2星）
label ch4_B2:
    scene bg_bedroom
    mc serious "那这样吧，货到付款，我收到平板验完货再付运费。"
    fraud serious "不行！公司规定必须先付运费才能出库，否则视为放弃奖品，卡片作废！"
    think serious "中奖的人反倒要抢着给对方付钱？越想越不对劲……"
    n "阿狐没有再理会。半小时后，对方头像变灰——账号已注销。"

    scene bg_living
    police serious "你坚持「先验货、后付款」，让骗子无处下手！记住：一听到货到付款就翻脸、逼你「先交钱」的，都是骗子。"

    $ clear_chapter(4, 2)
    $ quick_menu = False
    call screen level_clear(4, 2, l4_tip)
    $ quick_menu = True
    jump select_level


# B3：填写信息 · 轻微泄露（1星）
label ch4_B3:
    scene bg_bedroom
    n "阿狐按要求填写了姓名、电话和家庭住址，正准备扫码支付200元运费。"
    n "就在付款页面弹出的一瞬间，他突然想起老师的反诈课堂：领奖先交钱的，都是诈骗！"
    think serious "等等！我中大奖了，怎么还要我倒贴钱？不对劲！"
    mc serious "我不付了，你是骗子！"
    n "阿狐立刻把事情告诉妈妈。妈妈拉黑了对方，并叮嘱：以后收件人只写妈妈的名字和电话，住址不能随便告诉陌生人。"

    scene bg_living
    police serious "虽然没付钱，但姓名、电话、住址已经泄露！骗子可能实施「快递理赔」「冒充客服」等二次诈骗，以后收到陌生电话短信一定要多个心眼。"

    $ clear_chapter(4, 1)
    $ quick_menu = False
    call screen level_clear(4, 1, l4_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch4_C:
    scene bg_bedroom
    n "阿狐生怕错过大奖，赶紧追问领奖流程。"
    think laugh "平板电脑我来了，可千万别过期！"
    mc laugh "你好！我要领奖，需要怎么操作？我马上就办！"
    fraud laugh "真爽快！请您扫码支付200元「好运运费」，付完立刻进入发货队列！"

    menu:
        "付款前猛然醒悟，拒绝扫码":
            jump ch4_C1
        "心存侥幸，只付200元运费试试":
            jump ch4_C2
        "运费、公证费全部付清，坐等平板":
            jump ch4_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch4_C1:
    scene bg_bedroom
    n "手指刚要点开付款页面，阿狐心里突然咯噔一下。"
    think serious "不对！是我中奖，为什么反过来要我给对方付钱？领奖先交钱的就是骗子！"
    mc serious "奖品我不要了！往别人快递里塞假中奖卡骗人，我要举报你！"
    n "阿狐果断退出对话、举报账号，把整件事告诉了妈妈。妈妈夸了他，还提醒驿站和邻居注意。"

    scene bg_living
    police serious "面对「到手的奖品」还能保持清醒，非常了不起！记住：所有中奖诈骗都是拿「大奖」当诱饵，骗你先交「小钱」。"

    $ clear_chapter(4, 3)
    $ quick_menu = False
    call screen level_clear(4, 3, l4_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch4_C2:
    scene bg_bedroom
    n "阿狐既怕奖品作废，又有点不放心，决定先付200元运费试试。"
    think laugh "先付运费，平板发货了再说，应该没事吧。"
    n "200元转了过去。紧接着对方又发来消息。"
    fraud serious "系统提示：您的奖品还需缴纳200元「公证费」才能出库，请继续支付！"
    mc confused "怎么又冒出一个公证费？到底还有多少项收费？"
    n "阿狐越想越不对，把事情告诉妈妈。妈妈说这是典型的连环收费骗局，那200元已经追不回来了。"

    scene bg_living
    police serious "骗子的收费名目永远「还差最后一项」！只要付了第一笔，就会被一步步套牢。中奖缴费，一分都不能出！"

    $ clear_chapter(4, 1)
    $ quick_menu = False
    call screen level_clear(4, 1, l4_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch4_C3:
    scene bg_bedroom
    n "阿狐深信不疑，先付200元运费，又付200元「公证费」，一共400元，满心期待等平板到家。"
    n "第二天，阿狐催问发货，对方让他再付500元「关税押金」，说是付完连奖品带押金一起退。"
    mc confused "怎么一直要交钱？说好的平板呢？"
    n "阿狐再发消息，页面弹出红色感叹号——已被拉黑，「客服」账号也已注销。"
    think sad "说好的平板电脑呢……我把妈妈给的零花钱全搭进去了……"
    n "阿狐哭着向妈妈承认了错误，妈妈抱了抱他。"
    mom normal "没关系，这次教训要记牢。刮刮卡、中奖短信都是骗局的诱饵，以后涉及钱的事，一定先问爸爸妈妈。"

    scene bg_bedroom
    police serious "小朋友记住！「快递刮刮卡中奖」专骗中小学生：先用假大奖让你心动，再用运费、公证费、关税层层收钱。领奖先交钱，就是诈骗！"

    $ quick_menu = False
    call screen level_fail(4, l4_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch4
    else:
        jump select_level
