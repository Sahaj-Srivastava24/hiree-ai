import type {Metadata} from 'next';

import Layout from '@/lib/components/layout';
import {fontSans} from '@/lib/styles/fonts';
import cn from '@/lib/utils/tw-merge';

import '@/lib/styles/globals.css';

const APP_NAME = 'HireAI | Resume Parser';

export const metadata: Metadata = {
  title: APP_NAME,
  description:
    'The Resume Parser is a sophisticated tool designed to extract essential information from resumes and CVs in various formats, enabling efficient recruitment processes. With its advanced natural language processing and data extraction capabilities, the Resume Parser offers an invaluable solution for automating candidate information intake and analysis. ',
  viewport: {
    width: 'device-width',
    initialScale: 1,
  },
  applicationName: APP_NAME,
  appleWebApp: {
    capable: true,
    title: APP_NAME,
    statusBarStyle: 'default',
  },
  formatDetection: {
    telephone: false,
  },
  themeColor: '#FFFFFF',
};

interface RootLayoutProps {
  children: React.ReactNode;
}

const RootLayout = ({children}: RootLayoutProps) => {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={cn(
          'min-h-screen bg-background font-sans antialiased',
          fontSans.variable
        )}
      >
        <Layout>
          <div className="flex-1">{children}</div>
        </Layout>
      </body>
    </html>
  );
};

export default RootLayout;
