'use client';

import type { NextPage } from 'next';

import DragAndDrop from '@/lib/components/ui/drag-and-drop';

const Home: NextPage = () => {
  return (
    <article className="flex flex-col items-center w-full min-w-[60vw]">
      <section className="flex flex-col items-center justify-center text-center w-full bg-CE6F8FC rounded-lg text-C31327A px-12">
        <div className="flex flex-col gap-8 mt-10">
          <h1>
            Resume Parser at your <br />
            Fingertips
          </h1>
          <h6>Let us find the perfect candidates for your open positions.</h6>
        </div>

        <div className="relative top-20 rounded-lg p-6 bg-white">
          <DragAndDrop />
        </div>
      </section>

      <div className="flex items-center justify-between flex-row gap-8 w-[550px] h-30 font-bold rounded-lg mt-32 text-[14px] bg-[#FE9D8933] py-10 px-10">
        <p>Do you want to get unlimited parses..?</p>
        <button
          type="button"
          className="text-white bg-C31327A w-[160px] py-2 px-4 rounded-lg "
        >
          Create an account
        </button>
      </div>
    </article>
  );
};

export default Home;
