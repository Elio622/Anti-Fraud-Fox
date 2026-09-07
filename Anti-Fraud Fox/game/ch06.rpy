# game/ch06.rpy
#
# 关卡6：粉丝福利诈骗（假明星粉丝群抽奖）

define l6_tip = "粉丝福利套路深，扫码抽奖要当心，身份证脸不上交，先交钱的奖是坑！"


label ch6:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周五晚上，阿狐最喜欢的动画片周年庆，官方粉丝群炸开了锅。"
    n "一个头像是动画明星、昵称「官方福利君」的账号，在群里发起了「生日福利抽奖」。"
    fraud laugh "周年庆福利来啦！扫码进抽奖群，免费抽签名周边、限量手办、生日会门票，100%%中奖，仅限今天！"
    think laugh "签名手办！官方发的福利，不抽白不抽！"

    # === 第一轮抉择 ===
    fraud serious "抽奖通道2小时后关闭，扫码从速！"

    menu:
        "想起老师的话：官方福利只在官方渠道，退出群聊":
            jump ch6_A
        "问一问：免费抽奖为什么还要扫码进群？":
            jump ch6_B
        "机会难得，赶紧扫码进抽奖群":
            jump ch6_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch6_A:
    scene bg_bedroom
    n "阿狐盯着「扫码进群」四个字，突然想起老师反诈课上的提醒。"
    think serious "老师说过，明星官方活动只会在官方账号和官方平台发布，群里突然冒出来的「官方福利」，多半是假的！"
    mc serious "真官方不会在粉丝群里拉人扫码抽奖，这个「福利君」是假冒的！"
    n "阿狐不仅退出群聊，还截图举报了该账号，提醒群里的小粉丝们别上当。"
    n "没过两天，群里真的有同学中了这种假抽奖的招，交了「邮费」却被拉黑。"

    scene bg_living
    police laugh "警惕性满分！假冒「官方福利君」的骗子，最爱在粉丝群里用「免费抽奖」钓鱼。记住：真福利走官方渠道，群里扫码抽奖，一律是陷阱！"

    $ clear_chapter(6, 3)
    $ quick_menu = False
    call screen level_clear(6, 3, l6_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch6_B:
    scene bg_bedroom
    mc confused "官方抽奖不是在官方APP里吗？为什么要扫码加群呀？"
    fraud laugh "这次福利太火爆，官方APP抢不到，所以开设了「内部抽奖群」！你是第38位幸运粉丝，概率超高哦！"
    n "对方发来几张「粉丝中奖晒单」和仿官方的「活动海报」，看着像模像样。"
    fraud serious "登记抽奖资格需要：家长手机号、身份证号，再扫脸认证，防止黄牛冒领。信息绝对保密！"

    menu:
        "拿不准，先去问妈妈":
            jump ch6_B1
        "拒绝提供身份证和扫脸，退出群聊":
            jump ch6_B2
        "为了抽手办，按对方要求登记信息":
            jump ch6_B3


# B1：求助家长 · 满分
label ch6_B1:
    scene bg_living
    n "阿狐心里拿不准，拿着平板走到客厅找妈妈。"
    think worried "虽然好想要手办，但「扫脸认证」听起来有点吓人，还是先问问妈妈。"
    mc worried "妈妈，粉丝群有人办抽奖，要家长的手机号和身份证号，还要扫脸，是真的吗？"
    mom serious "宝贝，这是「粉丝福利」骗局！抽奖为什么要你的身份证和脸？那是拿去注册账号、开支付账户用的！真官方活动从来不需要这些。"
    n "妈妈陪阿狐举报了账号。第二天，那个「福利君」果然因诈骗被平台封禁。"

    scene bg_bedroom
    police laugh "问得及时！身份证号和人脸信息是身份的「钥匙」，谁要都不能给。你守住了最重要的信息，非常棒！"

    $ clear_chapter(6, 3)
    $ quick_menu = False
    call screen level_clear(6, 3, l6_tip)
    $ quick_menu = True
    jump select_level


# B2：拒绝提供信息 · 及时止损（2星）
label ch6_B2:
    scene bg_bedroom
    mc serious "抽个奖而已，凭什么要身份证号还要扫脸？这个我不参与。"
    fraud serious "不登记就等于放弃资格！多少人排队想要名额呢，错过今天就没有了！"
    think serious "越是不让犹豫、催得越紧的，越可疑。不填就是不填！"
    n "阿狐退出群聊并举报。几天后，新闻里报道了同款「粉丝抽奖」骗局，专骗小朋友的身份证信息去注册网络账号。"

    scene bg_living
    police serious "守住身份证号和扫脸这一关，你就守住了身份安全！骗子拿不到你的身份信息，后面的骗局就演不下去了。"

    $ clear_chapter(6, 2)
    $ quick_menu = False
    call screen level_clear(6, 2, l6_tip)
    $ quick_menu = True
    jump select_level


# B3：登记信息 · 轻微泄露（1星）
label ch6_B3:
    scene bg_bedroom
    n "为了心爱的手办，阿狐按对方要求填了妈妈的手机号和自己的身份证号。"
    n "刚提交，对方又发来消息：扫脸认证失败，需缴纳30元「人工认证费」重新审核。"
    think serious "等等……怎么又冒出认证费？老师说过，抽奖要交钱就是诈骗！"
    mc serious "我不交钱了，你们是骗子！"
    n "阿狐立刻告诉妈妈。妈妈马上修改了手机号关联的账户密码，并叮嘱身份证信息泄露可不是小事。"

    scene bg_living
    police serious "好险！身份证号和手机号已经泄露，骗子可能拿去注册账号甚至网贷。个人信息是底线，再心爱的奖品也不能拿信息去换！"

    $ clear_chapter(6, 1)
    $ quick_menu = False
    call screen level_clear(6, 1, l6_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch6_C:
    scene bg_bedroom
    n "阿狐扫码进了「抽奖群」，满心期待。"
    think laugh "限量手办，我来了！"
    fraud laugh "恭喜！系统显示你中了三等奖：签名手办一套！价值588元哦！"
    fraud serious "领取只需支付88元「粉丝会费+保价邮费」，付完48小时内发货！"

    menu:
        "付款前猛然醒悟，退出抽奖群":
            jump ch6_C1
        "心存侥幸，先付88元邮费试试":
            jump ch6_C2
        "怕到手的手办飞了，立刻付款":
            jump ch6_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch6_C1:
    scene bg_bedroom
    n "手指悬在付款按钮上方，阿狐心里突然咯噔一下。"
    think serious "不对！免费抽奖，怎么领奖反而要我交钱？老师说过，先交钱的奖全是坑！"
    mc serious "手办我不要了！假冒官方骗粉丝的钱，我要举报你！"
    n "阿狐退出群聊、举报账号，还把骗局的截图发进班级群，提醒同学们别上当。"
    n "老师特意在班会上表扬了他。"

    scene bg_living
    police serious "用行动保护了全班同学，好样的！记住：天上不会掉手办，「免费抽奖」的背后，永远等着你先交钱。"

    $ clear_chapter(6, 3)
    $ quick_menu = False
    call screen level_clear(6, 3, l6_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch6_C2:
    scene bg_bedroom
    n "阿狐舍不得到手的「手办」，决定先付88元邮费。"
    think laugh "88元换588元的手办，值！"
    n "付款成功，对方却又发来消息：手办是海外限量版，需再缴150元「清关费」，否则包裹销毁。"
    mc confused "又来一项收费？这手办到底还发不发货？"
    n "阿狐把事情告诉妈妈，妈妈判断这是连环收费骗局，88元已无法追回，账号也注销拉黑了。"

    scene bg_living
    police serious "「免费抽奖」实为「付费陷阱」：会费、邮费、清关费……名目层出不穷。记住：凡是中奖后还要交钱的，果断抽身别恋战！"

    $ clear_chapter(6, 1)
    $ quick_menu = False
    call screen level_clear(6, 1, l6_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch6_C3:
    scene bg_bedroom
    n "阿狐怕手办「飞了」，先付88元会费邮费，又付150元「清关费」，接着按对方要求交了200元「未成年认证解冻金」……"
    n "三天过去，手办毫无音讯。阿狐再去问，聊天框只剩刺眼的红色感叹号——他被拉黑，「抽奖群」也解散了。"
    mc sad "我的零花钱……全喂了骗子……"
    n "阿狐哭着向妈妈坦白，妈妈安慰他后立刻报警。"
    mom normal "手办以后还能攒钱买，教训记住了就好。真官方活动不收费，收费的「福利」都是骗局。"

    scene bg_bedroom
    police serious "小朋友记住！「粉丝福利」骗局专挑喜欢明星动画的同学下手：假官方、假抽奖、假中奖，最后全是真收钱。追星要理智，掏钱要三思！"

    $ quick_menu = False
    call screen level_fail(6, l6_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch6
    else:
        jump select_level
