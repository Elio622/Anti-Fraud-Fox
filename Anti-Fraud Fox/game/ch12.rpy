# game/ch12.rpy
#
# 关卡12：校园贷诈骗（零门槛学生贷款）

define l12_tip = "未成年不能贷款，零门槛全是陷阱，放款先收费是诈骗，缺钱就找爸妈谈！"


label ch12:

    # === 前置剧情 ===
    scene bg_bedroom
    n "开学第一周，同桌换了一台最新款手机，全班都围过去看。阿狐越看越羡慕，自己的手机已经用了三年。"
    n "晚上刷视频，一条小广告弹了出来：「青春钱包——学生专享，零门槛秒借款，只需学生证，最快5分钟到账！」"
    think laugh "借3000块买手机，以后用零花钱慢慢还，好像很划算？"
    n "阿狐点了进去，加上了「贷款客服」。"

    # === 第一轮抉择 ===
    fraud laugh "同学好！学生专享通道，最高可借5000元，日息低至万分之五，一杯奶茶钱都不到！上传学生证和身份证照片就能开通，家长那边完全不用知道！"

    menu:
        "想起「未成年人不能借贷」，退出并举报":
            jump ch12_A
        "问一问：不用家长知道，真的可以吗？":
            jump ch12_B
        "主动上传证件，申请开通借款":
            jump ch12_C


# ============ 分支A：理智避险 · 满分通关 ============
label ch12_A:
    scene bg_bedroom
    n "「零门槛」「不用家长知道」这些字眼，让阿狐猛然想起班会课的内容。"
    think serious "老师说过：未成年人不能贷款，凡是面向学生的「网贷」，全都不正规！天上不会掉手机，掉下来的是陷阱！"
    n "开学第一课的班会上，猫头鹰老师敲着黑板强调过这件事。"
    teacher serious "「零门槛」「不用家长知道」的学生贷款，全是陷阱！借三千能滚成一万。记住：缺钱，就跟爸爸妈妈说！"
    mc serious "未成年人不能借贷，这种小广告违法，我不碰！"
    n "阿狐截图举报了广告，第二天还把这事告诉了班主任。老师在班会上专门讲了「校园贷」的危害，提醒全班同学。"

    scene bg_living
    police laugh "非常棒！「校园贷」专门盯着想要新手机、新球鞋的学生：零门槛是鱼饵，利滚利是深渊。记住：缺钱找爸妈，贷款绝不能碰！"

    $ clear_chapter(12, 3)
    $ quick_menu = False
    call screen level_clear(12, 3, l12_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch12_B:
    scene bg_bedroom
    mc confused "我是未成年人，不用家长同意，真的能借钱吗？"
    fraud laugh "当然能！我们是「学生特殊通道」，不看征信、不联系家长。只要上传身份证照片，再填一下爸妈的电话「做登记」，秒批！"
    n "对方发来几张「学生借款成功到账」的截图，还有人晒出了新手机。"
    fraud serious "今天开通还有新人红包500元抵扣券，名额只剩10个了！"

    menu:
        "拒绝上传身份证，退出小广告":
            jump ch12_B2
        "为了手机，上传了证件照片":
            jump ch12_B3
        "拿不准，先去问问爸爸":
            jump ch12_B1


# B1：求助家长 · 满分
label ch12_B1:
    scene bg_living
    n "阿狐拿着手机走到客厅找爸爸。"
    think worried "「不用家长知道」这句话，怎么听怎么别扭……还是先问爸爸。"
    mc worried "爸爸，有个APP说学生能零门槛借款，不用家长同意，是真的吗？"
    dad serious "儿子，这是「校园贷」骗局！未成年人法律上根本不能借贷，这种平台全是违法的。你看「日息万分之五」，实际算下来年利息高得吓人，借3000能滚成上万！"
    n "爸爸陪阿狐举报了广告，还给他算了笔利滚利的账。阿狐看完倒吸一口凉气。"

    scene bg_bedroom
    police laugh "问家长问对了！校园贷的本质是「高利贷陷阱」，专门坑没收入的学生。记住：身份证不能交、网贷不能碰、缺钱和家人商量！"

    $ clear_chapter(12, 3)
    $ quick_menu = False
    call screen level_clear(12, 3, l12_tip)
    $ quick_menu = True
    jump select_level


# B2：拒绝上传证件 · 及时止损（2星）
label ch12_B2:
    scene bg_bedroom
    mc serious "身份证照片不能随便给。你们这种「不用家长知道」的贷款，一听就不正规，我不借了。"
    fraud serious "上传而已怕什么！没身份证就别怪平台没给你机会，红包名额马上没了！"
    think serious "越是催我交身份证的，越可疑。不传就是不传！"
    n "阿狐卸载了链接，举报了广告。后来新闻里报道了同款「青春钱包」骗局：学生上传证件后被冒名网贷、暴力催收。"

    scene bg_living
    police serious "守住身份证，就守住了底线！身份证照片一旦落入骗子手里，可能被冒名注册网贷、办卡，后患无穷。"

    $ clear_chapter(12, 2)
    $ quick_menu = False
    call screen level_clear(12, 2, l12_tip)
    $ quick_menu = True
    jump select_level


# B3：上传证件 · 轻微泄露（1星）
label ch12_B3:
    scene bg_bedroom
    n "阿狐按提示上传了身份证照片，还填了爸爸妈妈的电话号码。"
    n "刚提交，「客服」却发来消息：审核需先缴纳200元「工本费」，缴纳后3000元立刻放款。"
    think serious "等等！老师说，放款前先收费的都是诈骗！"
    mc serious "我不交了！你们是假的！"
    n "阿狐马上告诉爸爸。爸爸联系了相关平台投诉并报警备案——身份证照片已泄露，后续要格外提防冒名贷款。"

    scene bg_living
    police serious "好险！身份证信息已经泄露，骗子可能拿去冒名借款。记住两条铁律：放款先收费是诈骗，身份证照片不外传！"

    $ clear_chapter(12, 1)
    $ quick_menu = False
    call screen level_clear(12, 1, l12_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch12_C:
    scene bg_bedroom
    n "阿狐上传了身份证照片，填好资料，申请了3000元借款。"
    think laugh "5分钟到账，明天就能带新手机去学校了！"
    fraud laugh "恭喜，你的借款申请已通过初审！放款前最后一步：缴纳300元「会员费」激活账户，缴费后额度秒到！"
    fraud serious "注意：不缴费视为放弃借款，但合同已生效，将按借款金额的30%%收取违约金！"

    menu:
        "心存侥幸，先交300元会员费":
            jump ch12_C2
        "猛然醒悟：放款前收费的都是骗子":
            jump ch12_C1
        "怕被收违约金，乖乖交钱":
            jump ch12_C3


# C1：临危醒悟 · 逆风翻盘（3星）
label ch12_C1:
    scene bg_bedroom
    n "看着「缴费激活」的要求，阿狐心里突然咯噔一下。"
    think serious "不对！正规贷款是平台把钱给我，哪有借款人先给平台交钱的？老师说过，放款前收费的一律是诈骗！"
    mc serious "我不交钱，也不借了！未成年人借贷本来就不合法，你们这是欺诈，我要举报你们！"
    n "阿狐截图保留证据，退出平台，把整件事告诉爸爸。爸爸帮他向平台举报，并向反诈中心备案。"

    scene bg_living
    police serious "识破「合同违约金」的恐吓话术，非常出色！记住：贷款没到手先交钱的，全是诈骗；什么「违约金」「生效合同」，都是吓唬你的！"

    $ clear_chapter(12, 3)
    $ quick_menu = False
    call screen level_clear(12, 3, l12_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸妥协 · 轻微受害（1星）
label ch12_C2:
    scene bg_bedroom
    n "阿狐怕被收30%%违约金，咬牙交了300元「会员费」。"
    think laugh "300元换3000元借款，忍一忍就过去了。"
    n "缴费成功，对方却又发来通知：账户风控异常，需再缴800元「解冻金」才能放款，已缴费用不予退还。"
    mc confused "怎么交完会员费又冒出解冻金？"
    n "阿狐终于醒悟，把一切告诉爸爸。爸爸报警备案，300元已无法追回。"

    scene bg_living
    police serious "「校园贷」骗局专挑怕担责的孩子下手，用「违约金」吓你继续掏钱。记住：被吓住就转账，正中骗子下怀；告诉家长，才是唯一出路！"

    $ clear_chapter(12, 1)
    $ quick_menu = False
    call screen level_clear(12, 1, l12_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch12_C3:
    scene bg_bedroom
    n "阿狐被「30%%违约金」吓住，先交了300元会员费，又交了800元解冻金、500元「征信保险费」……"
    n "借款始终没到账，欠款「账单」却越滚越大：平台发来恐吓消息，说要上门催收、通知学校、打爆爸妈电话。"
    n "阿狐不敢告诉家人，偷偷把攒的压岁钱和零花钱全填了进去，前前后后被骗走2600元，手机没买成，整个人恍恍惚惚。"
    n "直到班主任发现他上课总走神，耐心询问，他才哭着说出实情。老师和家长立刻报警。"
    mc sad "我不该碰什么校园贷的……越陷越深，好可怕……"
    mom normal "不怪你，是骗子太坏。以后缺什么、想要什么，都跟爸爸妈妈说，咱们一起想办法。"

    scene bg_bedroom
    police serious "小朋友记住！「校园贷」零门槛的背后是无底洞：先收费、再恐吓、越滚越多。未成年人绝不借贷，遇到威胁马上告诉家长和老师，警察会保护你！"

    $ quick_menu = False
    call screen level_fail(12, l12_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch12
    else:
        jump select_level
