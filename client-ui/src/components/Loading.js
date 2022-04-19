import React from "react";
import Lottie from "react-lottie";
import * as loadingAnimation from "../assets/loading.json";

const Loading = () => {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: loadingAnimation,
  };

  return <Lottie options={defaultOptions} height={350} width={350} />;
};

export default Loading;
