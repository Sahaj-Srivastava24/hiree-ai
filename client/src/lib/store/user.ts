import { create } from 'zustand';

interface UserStore {
  isLoggedIn: boolean;
  setLogin: (val: boolean) => void;
}

export const userStore = create<UserStore>((set) => ({
  isLoggedIn: false,
  setLogin: (val: boolean) => set((state) => ({ isLoggedIn: val })),
}));
