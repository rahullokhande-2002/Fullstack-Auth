export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center h-screen gap-4">

      <a
        href="http://127.0.0.1:8000/auth/login/google-oauth2/"
        className="px-6 py-3 bg-red-500 text-white rounded-lg"
      >
        Login with Google
      </a>

      <a
        href="http://127.0.0.1:8000/auth/login/github/"
        className="px-6 py-3 bg-black text-white rounded-lg"
      >
        Login with GitHub
      </a>

      <a
        href="http://127.0.0.1:8000/auth/login/facebook/"
        className="px-6 py-3 bg-blue-600 text-white rounded-lg"
      >
        Login with Facebook
      </a>

    </div>
  );
}
