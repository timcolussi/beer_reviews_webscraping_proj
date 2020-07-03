library(shinydashboard)

shinyUI(
    dashboardPage(
        skin = "yellow",
        dashboardHeader(
            title = "Beer Reviews"
        ),
        dashboardSidebar(
           sidebarMenu(
               menuItem("Overall", tabName = "overall", icon = icon('comments')),
               menuItem("By Style", tabName = "style", icon = icon('beer'))
           ) 
        ),
        dashboardBody(
            tabItems(
                tabItem(tabName = "overall",
                        print("all comment tabs here")),
                tabItem(tabName = "style",
                        print("add style dropdown and tabs for comments"),
                        selectInput("selected", label = "Choose a Style:",
                                    choices = choices,
                                    selected = "IPA")
                        )
        )
        
    )
)
)