# game/ch13.rpy
#
# 关卡13：虚假中奖诈骗（弹窗/短信假中奖）

define l13_tip = "天上不会掉手机，中奖先交钱是骗局，名单截图可伪造，弹窗链接不要理！"


label ch13:

    # === 前置剧情 ===
    scene bg_bedroom
    n "周日晚上，阿狐在平板上玩小游戏，玩得正起劲，屏幕突然弹出一个大转盘页面。"
    n "「恭喜您成为本平台第88888位用户，被抽中为幸运大奖得主：最新款手机一部＋888元现金红包！」"
    mc laugh "88888位用户就是我？我是天选之子吗！"
    n "页面下方写着：点击领取，验证身份后24小时内发放。"
    think laugh "手机加888元，这运气没谁了！"

    # === 第一轮抉择 ===
    n "点击领取后，页面跳转到「领奖登记中心」，同时一个「兑奖客服」发来了消息。"
    fraud laugh "恭喜幸运用户！请登记姓名、身份证号、手机号，并支付88元「公证费」激活大奖，24小时内发放！"

    menu:
        "问一问：领奖为什么还要交公证费？":
            jump ch13_B
        "大奖就在眼前，马上登记领奖":
            jump ch13_C
        "想起反诈口诀，关闭页面并举报":
            jump ch13_A


# ============ 分支A：理智避险 · 满分通关 ============
label ch13_A:
    scene bg_bedroom
    n "「公证费」三个字让阿狐的手停在了半空。"
    think serious "老师说，凡是中奖后还要先交钱的，全是诈骗！什么幸运用户，就是冲着填信息来的！"
    mc serious "玩个游戏突然「中大奖」，还要交钱登记——不用想，假的！"
    n "阿狐关闭页面、举报了弹窗广告，并提醒一起玩游戏的表弟别点。"
    n "后来表弟说，他同学点了同款弹窗，交了88元「公证费」就被拉黑了。"

    scene bg_living
    police laugh "反应满分！游戏里的「幸运弹窗」是钓鱼广告，专门收集个人信息、骗取「手续费」。记住：没参加过的抽奖，永远不可能中奖！"

    $ clear_chapter(13, 3)
    $ quick_menu = False
    call screen level_clear(13, 3, l13_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支B：好奇试探 · 进入第二轮 ============
label ch13_B:
    scene bg_bedroom
    mc confused "是我中奖，为什么领奖还要我先交88元公证费呀？"
    fraud laugh "这是《奖品发放管理条例》规定的！你看，这是官方「中奖名单」，你是第7位；这是今天别人缴公证费的记录，大奖都发出去啦！"
    n "对方发来一张「中奖名单」截图和一排「缴费凭证」，看着像模像样。"
    fraud serious "大奖只保留24小时，逾期自动作废并顺延给下一位幸运用户！"

    menu:
        "身份证号不填，公证费也不交，直接回绝":
            jump ch13_B2
        "拿不准，拿着平板去找妈妈":
            jump ch13_B1
        "相信名单，填身份信息登记领奖":
            jump ch13_B3


# B1：求助家长 · 满分
label ch13_B1:
    scene bg_living
    n "阿狐关掉对话，拿着平板走进客厅。"
    think worried "名单和缴费记录看着挺真的……可「先交钱」这一点，还是不对劲。问问妈妈吧。"
    mc worried "妈妈，玩小游戏弹窗说我中了手机，让我交88元公证费，你看这中奖名单是真的吗？"
    mom serious "宝贝，这是「虚假中奖」骗局！名单和缴费凭证都能批量伪造。真抽奖你根本没参加过，怎么会中奖？领奖交钱的，全是骗子。"
    n "妈妈陪阿狐举报了弹窗和账号。"

    scene bg_bedroom
    police laugh "带着证据问家长，做得漂亮！记住：所有「中奖名单」「兑奖凭证」都可以PS，唯一做不了假的，是「没参加过的抽奖不会中奖」！"

    $ clear_chapter(13, 3)
    $ quick_menu = False
    call screen level_clear(13, 3, l13_tip)
    $ quick_menu = True
    jump select_level


# B2：部分配合 · 及时止损（2星）
label ch13_B2:
    scene bg_bedroom
    mc serious "名单我不看，公证费我不交，身份证号更不能给。要么原路发放奖品，不然就当我没中。"
    fraud serious "不登记不缴费，就是自动弃奖！机会难得，再想想！"
    think serious "催得越急，越像骗子。弃奖就弃奖！"
    n "阿狐关闭页面并举报。24小时后，「兑奖客服」果然注销了账号——哪有什么下一位幸运用户。"

    scene bg_living
    police serious "不为「大奖」动摇，守住了信息和钱包！「弃奖恐吓」是骗子的最后通牒，识破了它，骗局就演不下去了。"

    $ clear_chapter(13, 2)
    $ quick_menu = False
    call screen level_clear(13, 2, l13_tip)
    $ quick_menu = True
    jump select_level


# B3：填写身份信息 · 轻微泄露（1星）
label ch13_B3:
    scene bg_bedroom
    n "阿狐在「登记中心」填了姓名、身份证号和手机号。"
    n "刚提交，页面显示：身份验证通过，请支付88元公证费激活大奖。"
    n "付款页面弹出的一瞬间，阿狐突然想起老师的反诈口诀：中奖先交钱，必是骗局！"
    think serious "等等！名单能造假，缴费记录也能造假，我不能交钱！"
    mc serious "我不交了，你们是骗子！"
    n "阿狐退出页面，把经过告诉妈妈。妈妈修改了关联账户密码，并叮嘱身份证号泄露要格外警惕冒名办卡。"

    scene bg_living
    police serious "好险！姓名、身份证号、手机号已经打包泄露给骗子，后续可能收到各种「精准诈骗」。没交钱算万幸，信息防线一定要筑牢！"

    $ clear_chapter(13, 1)
    $ quick_menu = False
    call screen level_clear(13, 1, l13_tip)
    $ quick_menu = True
    jump select_level


# ============ 分支C：主动上钩 · 进入第三轮 ============
label ch13_C:
    scene bg_bedroom
    n "阿狐把身份信息登记好，支付了88元「公证费」，坐等大奖。"
    think laugh "手机马上到手，还有888元红包！"
    fraud laugh "公证费已收到！系统正在为你准备奖品……"
    fraud serious "叮！税务提示：大奖需先缴纳299元「个人所得税」，缴纳后手机和888元红包一并发放，否则奖品作废并列入失信名单！"

    menu:
        "怕列入失信名单，赶紧缴税":
            jump ch13_C3
        "猛然醒悟：哪有让中奖人先垫税的？":
            jump ch13_C1
        "心存侥幸，再付150元「部分税款」":
            jump ch13_C2


# C1：临危醒悟 · 逆风翻盘（3星）
label ch13_C1:
    scene bg_bedroom
    n "看着「缴税」的要求，阿狐心里突然咯噔一下。"
    think serious "不对！老师说，中奖缴税是在发奖时扣除，从来不会让中奖人先垫付！先是公证费，又是个人所得税，这就是连环骗局！"
    mc serious "我不缴了！中奖交公证费、垫税款，全是你们编的名目，我要举报你！"
    n "阿狐退出对话、举报账号，把完整经过告诉妈妈。妈妈肯定了他的判断，还陪他向反诈平台提交了线索。"

    scene bg_living
    police serious "「中奖纳税」的常识掌握得非常扎实！记住：所有让你先垫付税费、公证费的中奖，全是诈骗。骗子的每一步收费，都是为了掏空你的钱包！"

    $ clear_chapter(13, 3)
    $ quick_menu = False
    call screen level_clear(13, 3, l13_tip)
    $ quick_menu = True
    jump select_level


# C2：侥幸试探 · 轻微受害（1星）
label ch13_C2:
    scene bg_bedroom
    n "阿狐舍不得已付的88元，决定再付150元「部分税款」表个诚意。"
    think laugh "先付一部分，把大奖稳住，剩下的慢慢说。"
    n "150元转过去，对方立刻发来新通知：税款必须一次性缴清，已缴部分自动转为「手续费」，不予退还。"
    mc confused "说好的部分税款，怎么又变成手续费了？"
    n "阿狐把事情告诉妈妈。妈妈判断是连环收费骗局，238元已无法追回。"

    scene bg_living
    police serious "骗子的收费名目会一直「变身」：公证费、税款、手续费……只要你在乎「已付的钱」，就会一直被牵着走。及时止损，才是保住钱包的唯一办法！"

    $ clear_chapter(13, 1)
    $ quick_menu = False
    call screen level_clear(13, 1, l13_tip)
    $ quick_menu = True
    jump select_level


# C3：完全轻信 · 标准被骗结局
label ch13_C3:
    scene bg_bedroom
    n "阿狐怕「列入失信名单」，又付了299元税款。"
    n "紧接着对方又以「红包提现手续费」「未成年人监护认证金」为由继续要钱，阿狐前前后后转了880元。"
    n "说好的手机没影，888元红包也提不出来。再发消息——红色感叹号，被拉黑了。"
    mc sad "手机没等到，还倒贴了880块……妈妈知道会伤心的……"
    n "阿狐向妈妈坦白了经过，妈妈陪他报警备案。"
    mom normal "记住：所有突然掉下来的「大奖」，都是鱼钩上的饵。"

    scene bg_bedroom
    police serious "小朋友记住！「虚假中奖」三部曲：假弹窗、假名单、连环收费。没参加过的抽奖不会中奖，中奖先交钱必是诈骗，弹窗链接一律不理！"

    $ quick_menu = False
    call screen level_fail(13, l13_tip)
    $ quick_menu = True
    if _return == "retry":
        # 重新挑战时清空上一轮的对话历史，不残留上次尝试的内容
        $ _history_list = []
        jump ch13
    else:
        jump select_level
