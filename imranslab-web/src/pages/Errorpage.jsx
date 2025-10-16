/** @format */

const Errorpage = () => {
  return (
    <>
      <section className="bg-white h-[650px] flex items-center justify-center py-32">
        <div className="text-start">
          <h1 className="text-6xl font-bold text-[#B3225F]">OOPS!</h1>
          <p className="text-2xl mt-4 text-gray-600">Page Not Found</p>
          <p className="mt-2 text-gray-500">
            The page you are looking for does not exist or has been moved.
          </p>
          <a
            href="/home"
            className="mt-6 inline-block px-6 py-3 bg-[#B3225F] text-white rounded-lg hover:bg-[#9f1d4c]"
          >
            Go to Home
          </a>
        </div>
        <div>
          <img src="https://i.ibb.co/93Y9TWVG/404.png" alt="404" />
        </div>
      </section>
    </>
  );
};

export default Errorpage;
