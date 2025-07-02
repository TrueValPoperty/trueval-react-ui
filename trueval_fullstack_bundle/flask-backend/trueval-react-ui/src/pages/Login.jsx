
import { useState } from "react"

export default function Login() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = async (e) => {
    e.preventDefault()
    const res = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ username, password }),
    })
    if (res.redirected) window.location = res.url
    else alert("Login failed")
  }

  return (
    <form onSubmit={handleLogin} className="p-6 max-w-md mx-auto">
      <h1 className="text-2xl mb-4">Login</h1>
      <input placeholder="Username" name="username" onChange={e => setUsername(e.target.value)} className="border p-2 w-full mb-3"/>
      <input type="password" placeholder="Password" name="password" onChange={e => setPassword(e.target.value)} className="border p-2 w-full mb-3"/>
      <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded">Login</button>
    </form>
  )
}
