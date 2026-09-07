# game/ch05.rpy
#
# 关卡5：网课退费诈骗（假冒客服主动退费）

define l5_tip = "退费不用先交钱，让交钱的都是骗，陌生APP不要下，退费事宜爸妈把关！"


label ch5:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周二晚上，阿狐正在写作业。半年前他上过一个网课，最近网上的传言说那家机构倒闭了。"
    n "突然，一个陌生账号发来好友申请，自称「XX网课客服」。"
    fraud laugh "同学你好！你之前报名的网课因政策调整全面停课，公司现在统一办理学费退费，你那笔1200元学费可以退哦！"
    think normal "咦，还有这种好事？那笔学费妈妈提过好几次呢。"

    # === 第一轮抉择 ===
    fraud laugh "办理很简单，加入我们的「退费服务群」，按老师指引操作，退费三天到账！"
    fraud serious "本次退费只受理3天，过期视为自动放弃，名额先到先得！"

    menu:
        "把消息拿给妈妈，让妈妈去核实":
            jump ch5_A
        "回复询问：退费为什么要进群办理？":
            jump ch5_B
        "错过就没了，主动申请进群退费":
            jump ch5_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch5_A:
    scene bg_living
    n "阿狐盯着「主动找上门的退费」，心里犯起了嘀咕：机构都倒闭了，谁还这么好心主动退钱？"
    think serious "学校反诈课讲过「主动退费」的骗局——越主动送钱的，越要小心！"
    n "班会上，猫头鹰老师正好讲过同类的案例。"
    teacher serious "骗子会冒充客服主动找你「退费」，先用甜头把你引进假平台。记住：主动找上门的退费，一律先通过官方渠道核实！"
    mc serious "妈妈，有人自称网课客服，说能退1200元学费，让你进群办理，是真的吗？"
    mom serious "宝贝，这是「网课退费」骗局！机构真要退费，会按原报名渠道联系家长，绝不会拉学生进群操作。妈妈明天打官方电话核实。"
    n "第二天妈妈拨通了官方客服电话——机构运营一切正常，从未有过「退费活动」，这是冒牌客服的骗局。"

    scene bg_bedroom
    police laugh "太棒了！「主动退费」是骗子最爱用的诱饵：先冒充客服送钱，再把家长引进假平台收割。主动找上门的「退费」，一律先官方核实！"

    $ clear_chapter(5, 3)
    $ quick_menu = False
    call screen level_clear(5, 3, l5_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch5_B:
    scene bg_bedroom
    mc confused "退费直接原路退回不就行了吗？为什么还要进群办理？"
    fraud serious "公司资金清算是特殊流程，必须由「退费专员」统一登记。你看，群里好多同学都退到账了！"
    n "对方拉阿狐进群，群里不断有人晒出「退费到账截图」，看起来热热闹闹。"
    fraud laugh "登记后还需下载我们指定的「回款APP」，在上面完成认购任务，本金和退费一起返还，很多家长都在做！"

    menu:
        "退出群聊，把截图拿给妈妈看":
            jump ch5_B1
        "发现APP不在官方应用商店，拒绝下载":
            jump ch5_B2
        "按指引下载APP，注册登记信息":
            jump ch5_B3


# B1：求助家长 · 满分
label ch5_B1:
    scene bg_living
    n "阿狐退出群聊，拿着妈妈的手机把聊天记录和截图给妈妈看。"
    think worried "群里都说退到账了，可妈妈说过，真退费不该这么麻烦……"
    mc worried "妈妈，这个退费群让我下载APP做认购任务，你看是真的吗？"
    mom serious "这是「退费引流」骗局！你看这些「到账截图」，全是批量伪造的。真退费只会原路退回，让你买「理财产品」才能退费的，全是诈骗。"
    n "妈妈带阿狐举报了群和账号，还到原机构官方渠道核实，确认根本没有退费这回事。"

    scene bg_bedroom
    police laugh "做得好！凡是「先做任务、先买证券」才能退费的，都是把退费当鱼饵的诈骗！求助家长，你就赢了大多数骗子。"

    $ clear_chapter(5, 3)
    $ quick_menu = False
    call screen level_clear(5, 3, l5_tip)
    $ quick_menu = True
    jump select_level


# B2：发现APP异常 · 及时止损（2星）
label ch5_B2:
    scene bg_bedroom
    n "阿狐按对方发的链接找了一下，发现这个「回款APP」在手机官方应用商店里根本搜不到，只能从陌生网址下载。"
    think serious "不对，正规APP都在官方商店，要从陌生网站装的，多半有问题！"
    mc serious "这个APP我不能装。退费请走官方原路退回，不然就算了。"
    fraud serious "不装APP就无法登记，你的退费名额马上作废，最后一小时了！"
    n "阿狐没有动摇，退出群聊并举报。当晚，群里的「退费同学」全都不见了——那都是骗子的托。"

    scene bg_living
    police serious "你识破了「野鸡APP」的套路！非官方渠道的APP，往往内藏木马，专门盗取银行卡信息。能拦住这一步，银行账户就安全了！"

    $ clear_chapter(5, 2)
    $ quick_menu = False
    call screen level_clear(5, 2, l5_tip)
    $ quick_menu = True
    jump select_level


# B3：下载注册 · 轻微泄露（1星）
label ch5_B3:
    scene bg_bedroom
    n "阿狐下载了陌生APP，用手机号注册，并按提示填写了姓名和身份证号，上传了「收款信息」。"
    n "刚提交，APP就弹出提示：账户异常，需先缴纳500元「解冻金」才能提现退费。"
    fraud serious "快交解冻金，不然你登记的资金会被冻结，退费作废！"
    think serious "等等！退费哪有反过来交钱的？老师说过，这是骗局！"
    mc serious "我不交了，你们是骗子！"
    n "阿狐卸载APP，把事情告诉妈妈。妈妈第一时间修改了相关密码，并到银行确认了账户安全。"

    scene bg_living
    police serious "好险！姓名、身份证号已经泄露，骗子随时可能冒用。记住：要你先交钱的「退费」全是诈骗，身份证号更不能随便填！"

    $ clear_chapter(5, 1)
    $ quick_menu = False
    call screen level_clear(5, 1, l5_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch5_C:
    scene bg_bedroom
    n "阿狐一心想着帮妈妈拿回学费，立刻申请进群。"
    think laugh "退回1200元，妈妈肯定夸我能干！"
    mc laugh "你好，我要办理退费，怎么操作？"
    fraud laugh "好嘞！先做一个「新手任务」热热身：认购100元证券，马上返你120元本金加奖励！"
    n "阿狐试着转了100元，账户里果然显示「可提现120元」，还能先提现到账！尝到甜头的他更加相信了。"
    fraud serious "现在开启「快速退费通道」：完成3000元认购任务，你的1200元退费和本金一起秒到账！"

    menu:
        "猛然醒悟：退费怎么越退越要交钱？":
            jump ch5_C1
        "心存侥幸，先垫付500元试试":
            jump ch5_C2
        "凑齐3000元垫付，完成最后一步":
            jump ch5_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch5_C1:
    scene bg_bedroom
    n "看着「再交3000」的要求，阿狐心里突然咯噔一下。"
    think serious "不对！退费是机构把钱还给我，怎么会反过来让我不断交钱？老师说过，先给甜头再收割，就是刷单诈骗的套路！"
    mc serious "不办了！真退费不会让用户先垫钱，你们是骗子，我要举报你们！"
    n "阿狐退出群聊、举报账号，把整件事一五一十告诉了妈妈。妈妈立刻向原机构官方渠道核实并报警备案。"
    mom laugh "你能识破「先甜后刀」的套路，太让妈妈骄傲了！"

    scene bg_living
    police serious "临「钱」不乱，识破连环套，好样的！记住：所有「做任务才能退费」的，都是披着退费外衣的刷单诈骗！"

    $ clear_chapter(5, 3)
    $ quick_menu = False
    call screen level_clear(5, 3, l5_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch5_C2:
    scene bg_bedroom
    n "阿狐舍不得前面的100元，决定再垫500元，凑够「任务进度」。"
    think laugh "再垫500，说不定3000的任务就能打折完成，退费就到手了。"
    n "500元转过去后，对方却发来新通知：任务金额不足，之前的款项全部冻结，需补齐3000元才能一次性解冻提现。"
    mc confused "怎么规则一直在变？说好的退费呢？"
    n "阿狐把事情告诉妈妈，妈妈立刻报警。那600元垫付款，早已被骗子转走。"

    scene bg_living
    police serious "骗子的规则永远是「还差一步」！刷单垫资就像无底洞，越填越深。追不回的600元，是给你的深刻一课。"

    $ clear_chapter(5, 1)
    $ quick_menu = False
    call screen level_clear(5, 1, l5_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch5_C3:
    scene bg_bedroom
    n "阿狐满心想着拿回1200元退费，把攒了三年的压岁钱3000元全部垫付进去。"
    n "转账成功，页面却弹出：操作超时，账户冻结，需再缴6000元「解冻金」，否则全部资金没收。"
    n "阿狐慌了，想找「客服」理论——聊天群已被解散，APP无法登录，客服账号拉黑了他。"
    mc sad "我的压岁钱……全没了……妈妈还不知道……"
    n "阿狐哭着向妈妈坦白了一切，妈妈抱了抱他，立刻报警。"
    mom normal "钱的事以后一定先告诉妈妈。机构真倒闭了也走法律程序退费，绝不会让你先垫钱。"

    scene bg_bedroom
    police serious "小朋友记住！「网课退费」骗局的三板斧：假冒客服送钱、拉群晒假截图、做任务垫资金。凡是让你先交钱才能退费的，百分之百是诈骗！"

    $ quick_menu = False
    call screen level_fail(5, l5_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch5
    else:
        jump select_level
