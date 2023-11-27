import asyncio 
import time


async def make_coffee():
    print("coffee prep....")
    await asyncio.sleep(2)
    print("coffee done")
    return "coffee func executed"



async def make_beagle():
    print("beagle prep.....")
    await asyncio.sleep(3)
    print("beagle done")
    return "beagle func executed"



async def main():
    start = time.time()

    # batch = asyncio.gather(make_coffee(), make_beagle())
    # coffee_result, beagle_result = await batch

    coffee_result = asyncio.create_task(make_coffee())
    beagle_result = asyncio.create_task(make_beagle())

    r1 = await coffee_result
    r2 = await beagle_result


    end = time.time()
    time_taken = end -start 
    print("time taken : ", time_taken)




if __name__ == "__main__":
    asyncio.run(main())

