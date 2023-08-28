'use client';

import Link from 'next/link';
import Logo from '../ui/logo-file';
import { userStore } from '@/lib/store/user';

const Header = () => {
  const { isLoggedIn } = userStore();

  return (
    <header className="z-10 w-full text-C31327A mt-4 mb-6">
      <section className="wrapper mx-auto flex items-center justify-between py-2">
        <Link href="/">
          <div className="flex gap-4">
            <Logo />
            <p className="font-bold text-xl">HireAI</p>
          </div>
        </Link>

        {isLoggedIn && (
          <div>
            <ul className="list-none flex space-x-5">
              <li className="mx-3 my-2">
                <Link href="/leaderboard">Leaderboard</Link>
              </li>
            </ul>
          </div>
        )}

        {!isLoggedIn && (
          <div>
            <ul className="list-none flex space-x-5">
              <li className="mx-3 my-2">
                <Link href="/login">Login</Link>
              </li>
              <li className="text-white bg-C31327A px-3 py-2 rounded-lg ">
                <Link href="/signup">Sign Up</Link>
              </li>
            </ul>
          </div>
        )}
      </section>
    </header>
  );
};

export default Header;
