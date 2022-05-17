# dcinside_title_analysis_using_elk
Analyze the title of post in dcinside using elk

Since I use powershell, I will explain based on powershell.

At first

```c
PS docker compose up -d
```

setting dockers using docker compose

And change the IP adress in 

**dcinside_title_analysis_using_elk/kibana/conifg/kibana.yml \
dcinside_title_analysis_using_elk/logstash/config/logstash.yml \
dcinside_title_analysis_using_elk/logstash/pipeline/logstash.conf**

to yours

And please enter it in order

```c
PS docker cp {your file dicretory}\dcinside_title_analysis_using_elk\elasticsearch\config elk_stack-elasticsearch-1:/usr/share/elasticsearch/
PS docker cp {your file dicretory}\dcinside_title_analysis_using_elk\logstash\config elk_stack-logstash-1:/usr/share/logstash/
PS docker cp {your file dicretory}\dcinside_title_analysis_using_elk\logstash\pipeline elk_stack-logstash-1:/usr/share/logstash/
PS docker cp {your file dicretory}\dcinside_title_analysis_using_elk\kibana\config elk_stack-kibana-1:/usr/share/kibana/
```

And restart the docker containers

Now go into the **dcinside_title_analysis_using_elk/DCinside_Data** and install the modules written in requirement.txt
and transform the inside of dcinside_data_extractor.py the way you want it to be, and then run it.

This will create a file named **dcinside_Log.txt**

And enter this
```c
PS docker cp {your file dicretory}\dcinside_title_analysis_using_elk\DCinside_Data\dcinside_Log.txt elk_stack-logstash-1:/usr/share/logstash/pipeline/
```

Your data is now stored in elasticsearch query and can be visualized using kibana like below.
(Slang has been edited)

![블아갤](https://user-images.githubusercontent.com/80047618/168803467-687fa8da-1f38-4acc-81d1-f7af8e547857.png)
