import asyncio
import httpx
import json

#'https://rickandmortyapi.com/api/episode/1'

async def get_episode(ep_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'https://rickandmortyapi.com/api/episode/{ep_id}')
        results.append(r.json())
        return
    

async def main():
    tasks = []
    for ep_id in range(1, 50):
        tasks.append(get_episode(ep_id))
    await asyncio.gather(*tasks)


results = []
asyncio.run(main())

with open('rickandmortyapi.json', 'w') as f:
    json.dump(results, f)

print(len(results))