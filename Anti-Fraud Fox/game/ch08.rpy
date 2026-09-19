# game/ch08.rpy
#
# 关卡8：虚假网购诈骗（低价假店 + 私下转账）

define l8_tip = "网购要走官方店，明显低价必有诈，私下转账没保障，先款后货全是坑！"


label ch8:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周五晚上，阿狐盯着购物软件里那套心心念念的限量漫画书——官方店早已售罄。"
    n "他试着搜索书名，刷出一家不起眼的小店：同款漫画，价格只要官方的一半，页面写着「现货秒发」。"
    mc laugh "还有这种好事？便宜一半！"
    n "店铺客服主动发来消息。"
    fraud laugh "同学好眼光！这套书全网断货，本店还剩最后3套，官方半价，先到先得！"

    # === 第一轮抉择 ===
    fraud serious "平台下单要排队抢，直接加我微信，私下下单还能再减20元！"

    menu:
        "问一问：为什么便宜这么多？还能再便宜？":
            jump ch8_B
        "主动加微信，私下下单抢优惠":
            jump ch8_C
        "觉得不对劲，退出小店并举报":
            jump ch8_A


# ============ 分支A：理智避险 · 满分通关 ============
label ch8_A:
    scene bg_bedroom
    n "阿狐盯着「半价现货」，心里犯起了嘀咕。"
    think serious "全班同学都在抢这套书，官方店秒空，这家小店凭什么有货还半价？老师说过，明显低于市场价的，多半是陷阱！"
    mc serious "便宜一半还「私下交易」，八成是假店。我还是在官方店蹲补货，或者请妈妈帮忙。"
    n "阿狐截图举报了这家小店，把想法告诉了妈妈。妈妈帮他设置了到货提醒，一周后官方店真的补了货。"

    scene bg_living
    police laugh "警惕性满分！「限量缺货+超低价」是假店的经典诱饵。记住：价格明显低于行情的「现货」，要么是假货，要么是骗局，下单务必走官方平台！"

    $ clear_chapter(8, 3)
    $ quick_menu = False
    call screen level_clear(8, 3, l8_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch8_B:
    scene bg_bedroom
    mc confused "为什么你家能比官方便宜一半？私下买为什么还能再减20？"
    fraud laugh "我们是厂家内部渠道，不用给平台交抽成，自然便宜！私下下单省的20元，就是平台抽成那部分，返给你！"
    n "对方发来一套高仿的「店铺页面」和一长串「买家好评」截图，看着无可挑剔。"
    fraud serious "机会稍纵即逝，加微信转定金50元，立马锁单发货！"

    menu:
        "拿不准，先去问问妈妈":
            jump ch8_B1
        "坚持官方平台下单，绝不私下转账":
            jump ch8_B2
        "相信好评，微信转了50元定金":
            jump ch8_B3


# B1：求助家长 · 满分
label ch8_B1:
    scene bg_living
    n "阿狐拿着手机到客厅找妈妈。"
    think worried "好评一大堆，看着挺靠谱的……可私下转账总感觉不踏实，还是问问妈妈。"
    mc worried "妈妈，这家店漫画半价，让我加微信私下转定金，你看靠谱吗？"
    mom serious "宝贝，这是「虚假网购」骗局！你看，这些好评截图的水印都是同一批，是批量伪造的。私下转账没有平台保护，钱一转，人就找不到了。"
    n "妈妈陪阿狐举报了店铺，带他在官方平台预约了补货通知。"

    scene bg_bedroom
    police laugh "做得对！网购认准官方平台，交易全程有保障。让你「绕开平台私下转账」的，十个有十个是骗子！"

    $ clear_chapter(8, 3)
    $ quick_menu = False
    call screen level_clear(8, 3, l8_tip)
    $ quick_menu = True
    jump select_level


# B2：坚持官方平台 · 及时止损（2星）
label ch8_B2:
    scene bg_bedroom
    mc serious "减20元我就不要了。交易必须走官方平台，下单、付款、售后都有保障。私下转账，我不参与。"
    fraud serious "官方平台没货！你爱买不买，最后3套马上被别人抢光了！"
    think serious "真卖家不怕平台监管，怕监管的一定有问题。"
    n "阿狐不再理会。两周后，班级里有同学在同款小店私下转账600元，钱转过去立刻被拉黑。"

    scene bg_living
    police serious "你守住了「平台交易」这条底线！平台担保就是你网购的「安全气囊」，谁劝你跳过平台，谁就想拆掉你的安全气囊！"

    $ clear_chapter(8, 2)
    $ quick_menu = False
    call screen level_clear(8, 2, l8_tip)
    $ quick_menu = True
    jump select_level


# B3：私下转定金 · 轻微受害（1星）
label ch8_B3:
    scene bg_bedroom
    n "阿狐看着满屏好评，信以为真，加了微信转了50元定金。"
    n "转账成功后，对方却让他再付全款260元，「凑单一起发货，不然定金不退」。"
    think serious "等等……定金都转了，怎么还要我付全款？说好的发货呢？"
    mc serious "我不付了，把定金退给我！"
    n "对方先是拖延，接着把阿狐拉黑了。50元定金打了水漂。"
    n "阿狐把事情告诉妈妈，妈妈帮他向平台举报了店铺。"

    scene bg_living
    police serious "50元买了个教训！骗子先骗「定金」再逼「全款」，就是为了层层收割。记住：私下转账没有售后，出了事维权都难！"

    $ clear_chapter(8, 1)
    $ quick_menu = False
    call screen level_clear(8, 1, l8_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch8_C:
    scene bg_bedroom
    n "阿狐怕错过「最后3套」，加了微信转了50元定金。"
    think laugh "半价漫画马上到手，全班第一份！"
    fraud laugh "定金收到！系统显示你的订单已进入发货队列！"
    fraud serious "叮！仓库提示你的订单状态异常，需再支付300元「订单激活费」解锁发货，否则定金和订单一并作废！"

    menu:
        "心存侥幸，先付100元试试":
            jump ch8_C2
        "猛然醒悟，拒绝「激活费」":
            jump ch8_C1
        "怕定金打水漂，全额支付激活费":
            jump ch8_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch8_C1:
    scene bg_bedroom
    n "看着「再付300」的要求，阿狐心里突然咯噔一下。"
    think serious "不对！哪有下单之后还要交「激活费」的？老师说过，付费名目一个接一个，就是连环骗局！"
    mc serious "我不付了！你是假卖家，退还我的定金，不然我举报你！"
    n "阿狐截图保留证据，向平台和市场监管渠道举报了这家店，并把经过告诉妈妈。妈妈补上了官方店的到货提醒。"

    scene bg_living
    police serious "及时止损、保留证据、依法举报，三步全对！记住：正常的网购，付款一次就结束，后面不停要钱的，全是骗局！"

    $ clear_chapter(8, 3)
    $ quick_menu = False
    call screen level_clear(8, 3, l8_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch8_C2:
    scene bg_bedroom
    n "阿狐舍不得50元定金和到手的漫画，决定先付100元「部分激活费」。"
    think laugh "先付100表个诚意，说不定卖家就给我发货了。"
    n "100元转过去，对方又发来消息：激活需全额300元，已付部分不予退还。"
    mc confused "说好的激活，怎么又要凑全额？"
    n "阿狐把事情告诉妈妈，妈妈判断是连环骗局，那150元已无法追回。"

    scene bg_living
    police serious "骗子的收费永远「还差最后一步」！对付连环骗局只有一招：一分钱都不要再付，马上止损、保留证据、告诉家长！"

    $ clear_chapter(8, 1)
    $ quick_menu = False
    call screen level_clear(8, 1, l8_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch8_C3:
    scene bg_bedroom
    n "阿狐怕定金作废，咬牙付了300元「激活费」。"
    n "对方又接连以「物流保证金」「未成年人订单审核费」为由要钱，阿狐前前后后转了650元，漫画始终没有踪影。"
    n "再发消息，微信显示：对方已开启朋友验证——他被拉黑了。那个小店，也在平台上消失了。"
    mc sad "漫画没买到，零花钱全没了……"
    n "阿狐向妈妈坦白了一切，妈妈陪他报了警，留了证据。"
    mom normal "记住这次教训：买东西宁可多等等，也绝不私下转账。"

    scene bg_bedroom
    police serious "小朋友记住！「虚假网购」两板斧：超低价引你上钩，绕开平台骗你转账。认准官方店铺，钱货两清走平台，私下转账都是坑！"

    $ quick_menu = False
    call screen level_fail(8, l8_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch8
    else:
        jump select_level
