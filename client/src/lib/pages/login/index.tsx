'use client';

import type {NextPage} from 'next';
import {useState} from 'react';
import * as Form from '@radix-ui/react-form';
import {useRouter} from 'next/navigation';
import Toast from '@/lib/components/ui/toast';
import {login} from '@/lib/utils/user-data';
import {userStore} from '@/lib/store/user';

const Login: NextPage = () => {
  const [openToast, setOpenToast] = useState(false);
  const {setLogin} = userStore();
  const router = useRouter();
  const [password, setPassword] = useState('');
  const [mail, setMail] = useState('');

  const handleSubmit = () => {
    console.log('submit ran');
    login(mail, password);
    setLogin(true);
    // window.location.href = 'localhost:8501';
    router.push('/')
  };

  return (
    <article className="flex flex-col items-center w-full min-w-[60vw]">
      <Toast
        text="Your file was not uploaded"
        open={openToast}
        setOpen={setOpenToast}
      />
      <section className="card w-1/2">
        <h1 className="text-center mb-8 text-C31327A">Log In</h1>
        <Form.Root className="" action="/">
          <Form.Field className="grid mb-[10px]" name="email">
            <div className="flex items-baseline justify-between w-full">
              <Form.Label className="text-[15px] font-medium leading-[35px] text-C31327A">
                Email
              </Form.Label>
              <Form.Message
                className="text-[13px] text-C31327A opacity-[0.8]"
                match="valueMissing"
              >
                Please enter your email
              </Form.Message>
              <Form.Message
                className="text-[13px] text-C31327A opacity-[0.8]"
                match="typeMismatch"
              >
                Please provide a valid email
              </Form.Message>
            </div>
            <Form.Control asChild>
              <input
                required
                value={mail}
                type="email"
                onChange={(e) => setMail(e.target.value)}
                className="box-border w-full bg-blackA5 shadow-blackA9 inline-flex h-[35px] appearance-none items-center justify-center rounded-[4px] px-[10px] text-[15px] leading-none text-C31327A shadow-[0_0_0_1px] outline-none hover:shadow-[0_0_0_1px_black] focus:shadow-[0_0_0_2px_black] selection:color-white selection:bg-blackA9"
              />
            </Form.Control>
          </Form.Field>
          <Form.Field className="grid mb-[10px]" name="question">
            <div className="flex items-baseline justify-between">
              <Form.Label className="text-[15px] font-medium leading-[35px] text-C31327A">
                Password
              </Form.Label>
              <Form.Message
                className="text-[13px] text-C31327A opacity-[0.8]"
                match="valueMissing"
              >
                Please enter a question
              </Form.Message>
            </div>
            <Form.Control asChild>
              <input
                required
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="box-border w-full bg-blackA5 shadow-blackA9 inline-flex appearance-none items-center justify-center rounded-[4px] p-[10px] text-[15px] leading-none text-C31327A shadow-[0_0_0_1px] outline-none hover:shadow-[0_0_0_1px_black] focus:shadow-[0_0_0_2px_black] selection:color-white selection:bg-blackA9 resize-none"
              />
            </Form.Control>
          </Form.Field>
          <Form.Submit asChild>
            <button
              onClick={handleSubmit}
              className="box-border w-full text-white shadow-blackA7 hover:bg-C31327A inline-flex h-[35px] items-center justify-center rounded-[4px] bg-C31327A px-[15px] font-medium leading-none shadow-[0_2px_10px] focus:shadow-[0_0_0_2px] focus:shadow-black focus:outline-none mt-[10px]"
            >
              Login
            </button>
          </Form.Submit>
        </Form.Root>
      </section>
    </article>
  );
};

export default Login;
