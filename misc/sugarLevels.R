#sugar levels  Glucose Levels of Vimla 

pacman::p_load(tidyverse, googlesheets4, lubridate, tidyr, chron, directlabels)

gs='1RN6VjO4EOj1ATRvpWuk9qDQbLXDgKi6MFcZG2EaMws0'
sheet_names(gs)
cTypes = 'cDticc____'
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

g1A <- sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value, group=dateTest)) + geom_line() + facet_wrap(dateTest ~ . ,scale='free')
g1A

T1='Daily Glucose Reading Patterns : Each Date Wise'
g1B <- sugar1 %>% arrange(dateTime) %>% group_by(dateTest = as.Date(dateTime), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value, group=1)) + geom_line(group=1, color='red') + facet_wrap(dateTest ~ . ,scale='free') + geom_point(size=.5) + geom_hline(yintercept = c(80,100,150,200,250,300), linewidth=.3, color='gray') + labs(ttile=T1) + geom_dl(aes(label = Value), method = list(dl.combine('top.points'), cex=.7))
g1B 

#---------------
sugar1 %>% arrange(dateTime) %>% group_by(month = month(dateTime, label=T), dateTest = as.Date(dateTime), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=timeTest, y=Value, group=dateTest)) + geom_line() + geom_point() + facet_wrap(dateTest ~ month ,scale='free') 


sugar1 %>% arrange(dateTime) %>% group_by(dateTest = strftime(dateTime, format='%d-%b'), timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% filter(!is.na(Value)) %>% ggplot(., aes(x=dateTime, y=Value)) + geom_line(aes(group=dateTest, color=dateTest)) + guides(color='none') + scale_x_datetime (labels=scales::date_format('%H')) + facet_wrap(dateTest ~ . ,scale='free') 

sugar1 %>% arrange(dateTime) %>% group_by(timeTest = strftime(round(dateTime,'hours'), format='%H%M') ) %>% summarise(count = n(), avg = mean(Value, na.rm=T)) %>% ggplot(., aes(x=timeTest, y=avg)) + geom_line(aes(group=1)) + guides(color='none') + geom_text(aes(label=paste(count ,'/ ', round(avg)))) + geom_vline(xintercept = c('0100','0300','0600','0800','0900','1300', '1500','1800', '2000','2200'), color='green', linewidth=.5) + geom_hline(yintercept = c(100, 150, 200), color='red') + labs(title='Sugar/Glucose Level Readings of Ms Vimla Upadhyaya - Last 3 months', subtitle = 'No of readings taken / Average reading during this hour')

sugar1 %>% arrange(dateTime) %>% filter(month(dateTime) == 6) %>% ggplot(., aes(x=dateTime, y=Value)) + geom_line(aes(group=1)) + guides(color='none') + geom_text(aes(label=Value)) + labs(title='Sugar/Glucose Level Readings of Ms Vimla Upadhyaya - Last 3 months', subtitle = 'No of readings taken / Average reading during this hour')                                                                                                                                                                                                                                                                  
sugar1
T1 ='Avg Glucose Readings in Apr-Jul 2023'
g4A <- sugar1 %>% group_by(Date, month= lubridate::month(Date, label=T))  %>% summarise(avgSugar = round(mean(Value, na.rm=T)), count= n())  %>% ggplot(., aes(x=Date, y=avgSugar)) + geom_line( aes(group=month, color=month)) + geom_point() + geom_text(aes(label = paste0(avgSugar, '(', count,')'))) + geom_hline(yintercept = c(100,150,200,250)) + labs(title=T1)  
g4A 

T1 ='Avg Daily Glucose Readings in Jun-Jul 2023 with count of readings taken on the day'
g4B <- sugar1 %>% filter(Date > as.Date('2023-06-01')) %>%  group_by(Date, month= lubridate::month(Date, label=T))  %>% summarise(avgSugar = round(mean(Value, na.rm=T)), count= n())  %>% ggplot(., aes(x=Date, y=avgSugar)) + geom_line( aes(group=month, color=month)) + geom_point() + geom_text(aes(label = paste0(avgSugar, '(', count,')'))) + geom_hline(yintercept = c(100,150,200,250)) +labs(title=T1) + scale_color_manual(values=c('green','red')) + scale_x_date(date_breaks = "1 day", date_minor_breaks = "1 day", date_labels = "%d %b") 
g4B

#time intervals----
#00:00-06:00, 06:00-09:00, 09:00-15:00, 15:00-20:00, 20:00-23:59
Sys.Date()+ days(1)
seconds(15)
(today() %--% as.Date('2023-01-01') ) %/% days(1)

time = format(sugar1$dateTime, format ='%H:%M')
time
class(time)
time2 =  lubridate::hms(sugar1$dateTime)
lubridate::hm(sugar1$dateTime)
?lubridate::hm
x <- c("09:10", "09:10:02", "09:10:03")
hm(x)
hm(time)
sugar1 %>% mutate(time_hms = as.character(lubridate::hm(format(dateTime, format ='%H:%M')))) %>% separate(col=time_hms, into=c('h'), sep='H', remove=F) %>% slice(270:281)
head(sugar1)
as.numeric(chron::times("09:13:00"))
ymd(20230715)
trunc(Sys.time() ,'days')
(sugar2  <- sugar1 %>% mutate(time_hms = lubridate::hms(format(dateTime, format ='%H:%M:%S')), time2 = format(dateTime, '%H:%M:%S')) %>% separate(col=time_hms, into=c('h','m','s'),  remove=F) )
(sugar2B <-  sugar2 %>% mutate(numTime = as.numeric(chron::times(time2)))  %>% arrange(desc(numTime)) %>% mutate(timeNum = chron(numTime, format=c(dates='dmy', times='h:m:s'))))

sugar2B %>% mutate(rmonth = lubridate::month(Date, label=T)) %>%  ggplot(., aes(x=numTime, fill= rmonth)) + geom_histogram() + facet_wrap(rmonth ~. )

breaks1 = c(0, .25, .5, .75, .999)
chron(breaks1, format=c(dates='dmy', times='h:m:s'))
sugar2B %>% mutate(rmonth = lubridate::month(Date, label=T), timePD = cut(numTime, breaks=breaks1, labels=c('0-6','6-12', '12-18','18-24')))  %>% group_by(rmonth, timePD)  %>% summarise(avgSugar = round(mean(Value, na.rm=T)), n=n())  %>% ggplot(., aes(x=timePD, y=avgSugar, fill=timePD)) + geom_bar(stat='identity') + geom_text(aes(label=paste0(avgSugar,'/',n))) + facet_grid(rmonth ~ . )

sugar2B %>% mutate(rmonth = lubridate::month(Date, label=T)) %>% ggplot(., aes(x=rmonth, y=Value, fill=rmonth)) + geom_violin(trim=FALSE) + stat_summary(fun.y=mean, geom="point", shape=23, size=2)+ geom_boxplot(width=0.1) + scale_fill_brewer(palette="Set2") + geom_jitter(shape=16, position=position_jitter(0.2)) +  scale_y_continuous(limits=c(1, 375))

T1='VU : Glucose Readings : Readings over 4 intervals(0-6am, 6-12pm, 12-6pm, 6-0am) in last few months'
g5A <- sugar2B %>% mutate(rmonth = lubridate::month(Date, label=T), timePD = cut(numTime, breaks=breaks1, labels=c('0-6','6-12', '12-18','18-24'))) %>% ggplot(., aes(x=timePD, y=Value, fill=rmonth))  + stat_summary(fun.y=mean, geom="point", shape=23, size=2)+ geom_boxplot(width=0.5) + scale_fill_brewer(palette="Set2") + geom_jitter(shape=16, position=position_jitter(0.2)) +  scale_y_continuous(limits=c(1, 375)) + facet_grid( . ~ rmonth ) + labs(title=T1)
g5A
