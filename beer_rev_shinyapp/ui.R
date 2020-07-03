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
                        tabsetPanel(type = "tabs",
                                    tabPanel("Brewer Comments", imageOutput("bc_all")),
                                    tabPanel("Panel Comments", imageOutput("pc_all")),
                                    tabPanel("Editor Comments", imageOutput("ec_all"))
                                    )
                ),
                tabItem(tabName = "style",
                        print("add style dropdown and tabs for comments"),
                        selectInput("selected", label = "Choose a Style:",
                                    choices = choices,
                                    selected = "IPA"),
                        tabsetPanel(type = "tabs",
                                    tabPanel("Brewers Comments", imageOutput("bc_style")),
                                    tabPanel("Panel Comments", imageOutput("pc_style")),
                                    tabPanel("Editor Comments", imageOutput("ec_style")))
                        )
        )
        
    
)
))