import Leaderboard from '@/lib/pages/leaderboard';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();
async function getRecords() {
  const entries = await prisma.dataEntry.findMany();
  console.log(entries);
}

const Page = async () => {
  const res = getRecords();

  return <Leaderboard />;
};
export default Page;
