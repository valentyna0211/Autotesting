from pages.base_page import BasePage


class Dashboard(BasePage):
    Page_title = "//*[@class='MuiCardHeader-content']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    My_team_input = "'// input[ @ name = 'myTeam']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    My_enemy_input ="//input[@name='enemyTeam']"
        #  "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    My_team_score_input = "//input[@name='myTeamScore']"
        #  "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    Enemy_team_score_input = "//input[@name='enemyTeamScore']"
        #  "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    Date = "//input[@name='date']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    Match_at_home_radiobutton = "//input[@name='matchAtHome'][@value='true']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]"
    Match_out_home_radiobutton ="//input[@name='matchAtHome'][@value='false']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]"
    T_shirt_color ="//input[@name='tshirt']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    League_input = "//input[@name='league']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
    Time_played = "//input[@name='timePlayed']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    Numbers = "//input[@name='number']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    Web_match = "//input[@name='webMatch']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    General = "'//input[@name='general']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    Raiting = "//input[@name='rating']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    Submit_button = "//button[@type='submit']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
    Clear_button = "//*[text()='Clear']"
        #"//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[2]"

    pass





# Side Pane Elements
#     Main_page_item = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]"
#     Players_item = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
#     Language_item = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
#     Sign_out_item = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"