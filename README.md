## Task 1: software configuration.
__Subtask 1: Why did I choose to participate in the Dare IT Challenge?__\
I'm interested in autotesting, and the course exactly what I was looking for.\
\
Goals of the course:
- Learn prinsiples of programing 
- Study approches in autotesting
- Use knowlage on practise
## Task 2: Selectors.
__Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.__\
\
Page title "Scouts Panel":
- "//*[@id='__next']/form/div/div[1]/h5"
- "h5.MuiTypography-root.MuiTypography-h5"
- "h5.MuiTypography-root.MuiTypography-h5.MuiTypography-gutterBottom"

Login label:
- "#login-label"
- "//*[@id='login-label']"

Login Input:
- "//*[@id='login']"
- "input#login.MuiInputBase-input.MuiInput-input"
- "/html/body/div/form/div/div[1]/div[1]/div/input"

Password Label:
- "#password-label"
- "//*[@id='password-label']"
- "/html/body/div/form/div/div[1]/div[2]/label"

Password Input:
- "#password"
- "//*[@id='password']"
- "/html/body/div/form/div/div[1]/div[2]/div/input"

Remind Password Link:
- "a.MuiTypography-root.MuiLink-root.MuiLink-underlineHover.jss29.MuiTypography-colorPrimary"
- "#__next > form > div > div.MuiCardContent-root > a"
- "//*[@id='__next']/form/div/div[1]/a"
- "/html/body/div/form/div/div[1]/a"

Language Dropdown:
- "div.MuiSelect-root.MuiSelect-select.MuiSelect-selectMenu"
- "//*[@id='__next']/form/div/div[2]/div/div"
- "//*[@id='__next']/form/div/div[2]/div/input" \
(expand dropdown)
- "ul.MuiList-root.MuiMenu-list.MuiList-padding"
- "//*[@id='menu-']/div[3]/ul/li[1]" (polish lang. option)
- "//*[@id='menu-']/div[3]/ul/li[2]" (eng.lang. option) \
arrow icon
- "//*[@id='__next']/form/div/div[2]/div/svg"
- "svg.MuiSvgIcon-root.MuiSelect-icon"
- "svg.MuiSvgIcon-root.MuiSelect-icon.MuiSelect-iconOpen" (icon open)

Sign In Button:
- "#__next > form > div > div.MuiCardActions-root > button > span.MuiButton-label"
- "span.MuiButton-label"
- "//*[@id='__next']/form/div/div[2]/button/span[1]"