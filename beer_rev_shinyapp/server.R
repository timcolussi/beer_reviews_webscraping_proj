shinyServer(
    function(input, output) {
        output$bc_all <- renderImage({
            filename <- normalizePath(file.path('./www/bc_token_stem_lem_all.png'))
            list(src = filename)
        }, deleteFile = FALSE)
        output$pc_all <- renderImage({
            filename <- normalizePath(file.path('./www/pc_token_stem_lem_all.png'))
            list(src = filename)
        }, deleteFile = FALSE)
        output$ec_all <- renderImage({
            filename <- normalizePath(file.path('./www/ec_token_stem_lem_all.png'))
            list(src = filename)
        }, deleteFile = FALSE)
        output$bc_style <- renderImage({
            filename <- normalizePath(file.path('./www',
                                                paste0('bc_token_stem_lem_', tolower(input$selected), '.png')))
            list(src = filename)
        }, deleteFile = FALSE)
        output$pc_style <- renderImage({
            filename <- normalizePath(file.path('./www',
                                                paste0('pc_token_stem_lem_', tolower(input$selected), '.png')))
            list(src = filename)
        }, deleteFile = FALSE)
        output$ec_style <- renderImage({
            filename <- normalizePath(file.path('./www',
                                                paste0('ec_token_stem_lem_', tolower(input$selected), '.png')))
            list(src = filename)
        }, deleteFile = FALSE)
    }
)


# 
# output$plot3 <- renderImage({
#     # When input$n is 1, filename is ./images/image1.jpeg
#     filename <- normalizePath(file.path('./images',
#                                         paste('image', input$n, '.jpeg', sep='')))
#     
#     # Return a list containing the filename
#     list(src = filename)
# }, deleteFile = FALSE)
# 
# list(src = "http://data-informed.com/wp-content/uploads/2013/11/R-language-logo-224x136.png",
#      contentType = 'image/png',
#      width = 224,
#      height = 136,
#      alt = "This is image alternate text")