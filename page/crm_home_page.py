from poium import Page, PageElement


class GfyHomePage(Page):
    home_index_menu = PageElement(
        xpath="//*[@id=\"sysMenu\"]/li[1]/a/span", describe="系统菜单-首页")
    more_home_remind = PageElement(
        css="button.pull-right:nth-child(2)", describe="待办消息信息-更多")
    home_remind_params = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[1]/div/select",
        describe="提醒消息-题型类型")
    remind_content_search = PageElement(
        xpath="/html/body/div[1]/div[1]/div[1]/section[2]/div[1]/form/div[4]/div/input",
        describe="提醒消息-消息内容查找")
