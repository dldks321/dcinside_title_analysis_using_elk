import dc_api
import asyncio

async def dcinside_data_extract() :
    api = dc_api.API()

    #Change the variable as many data as you want
    need_data = 5000

    count = 1

    ''' board_id =>
        https://gall.dcinside.com/mgallery/board/lists?id=projectmx
        input something like "projectmx" '''    
    async for index in api.board(board_id="programming", num=-1, start_page=1, document_id_upper_limit=None, document_id_lower_limit=None):
        #break the title of the article into words
        for token in index.title.split(" ") :
            save_file.write(token)
            save_file.write("\n")
        
        if(count >= need_data) : 
            break
        
        count += 1

if(__name__ == '__main__') :
    save_file = open("dcinside_Log.txt","w",encoding='UTF-8')
    asyncio.run(dcinside_data_extract())
    save_file.close()
