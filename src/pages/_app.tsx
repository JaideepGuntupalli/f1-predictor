import { type AppType } from "next/app";

import { api } from "src/utils/api";

import "src/styles/globals.css";

const MyApp: AppType = ({ Component, pageProps }) => {
  return <Component {...pageProps} />;
};

export default api.withTRPC(MyApp);
