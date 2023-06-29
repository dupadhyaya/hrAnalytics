#sugar levels


pacman::p_load(tidyverse, googlesheets4)

gs='1RN6VjO4EOj1ATRvpWuk9qDQbLXDgKi6MFcZG2EaMws0'
sheet_names(gs)
cTypes = 'cDticc___'
nchar(cTypes)
sugar = read_sheet(ss=gs, sheet='2023', skip=1, col_types = cTypes)
sugar

sugar1 <- sugar %>% mutate(time = format(as.POSIXct(Time), format='%H:%M'))  %>% select(-Time) %>% mutate(dateTime = as.POSIXct(paste(format(Date, '%Y-%m-%d') , time)))
sugar %>% mutate(time = round(as.POSIXct(Time), 'mins')) 

head(sugar1)
sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'), timeTest = strftime(dateTime, format='%H%M') )  %>% summarise(n=n(), avg = mean(Value, na.rm=T))

sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'))  %>% summarise(n=n(), avg= mean(Value, na.rm=T))

sugar1 %>% arrange(dateTime) %>% group_by(dateTest = month(dateTime, label=T)) %>% summarise(n=n(), avg = mean(Value, na.rm=T), min = min(Value, na.rm=T), max=max(Value, na.rm=T))

sugar1 %>% arrange(dateTime) %>% summarise(n=n(), avg = mean(Value, na.rm=T))

hist(sugar1$Value)

sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value, group=dateTest)) + geom_line() + facet_wrap(dateTest ~ . ,scale='free')

sugar1 %>% arrange(dateTime) %>% group_by(month = month(dateTime, label=T), dateTest = as.Date(dateTime), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value, group=dateTest)) + geom_line() + geom_point() + facet_wrap(dateTest ~ month ,scale='free') 


sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value)) + geom_line(aes(group=dateTest, color=dateTest)) + guides(color='none')

sugar1 %>% arrange(dateTime) %>% group_by(timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% summarise(count = n(), avg = mean(Value, na.rm=T)) %>% ggplot(., aes(x=timeTest, y=avg)) + geom_line(aes(group=1)) + guides(color='none') + geom_text(aes(label=paste(count ,'/ ', round(avg)))) + geom_vline(xintercept = c('0100','0300','0600','0800','0900','1300', '1500','1800', '2000','2200'), color='green', linewidth=.5) + geom_hline(yintercept = c(100, 150, 200), color='red') + labs(title='Sugar/Glucose Level Readings of Ms Vimla Upadhyaya - Last 3 months', subtitle = 'No of readings taken / Average reading during this hour')

sugar1 %>% arrange(dateTime) %>% filter(month(dateTime) == 6) %>% ggplot(., aes(x=dateTime, y=Value)) + geom_line(aes(group=1)) + guides(color='none') + geom_text(aes(label=Value)) + labs(title='Sugar/Glucose Level Readings of Ms Vimla Upadhyaya - Last 3 months', subtitle = 'No of readings taken / Average reading during this hour')                                                                                                                                                                                                                                                                  
