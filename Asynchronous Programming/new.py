import time
import asyncio



async def coffee():
    print("making coffee")
    await asyncio.sleep(5)
    print("coffee done!")
    return "coffee func done!"



async def beagle():
    print("making beagle")
    await asyncio.sleep(4)
    print("beagle done!")
    return "beagle func done!"


async def main():
    start = time.time()

    # ### method - 1 (using gather)
    # batch =  asyncio.gather(coffee(), beagle())
    # result_coffee, result_batch = await batch


    ### method - 2 (using create_task)
    coffee_task = asyncio.create_task(coffee())
    beagle_task = asyncio.create_task(beagle())

    result_coffee = await coffee_task
    result_beagle = await beagle_task

    end = time.time()
    time_taken = end - start
    print(f"time taken : {time_taken}")


if __name__ == "__main__":
    asyncio.run(main())
