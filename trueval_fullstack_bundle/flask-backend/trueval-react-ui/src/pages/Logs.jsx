
import { useEffect, useState } from "react"

export default function Logs() {
  const [logs, setLogs] = useState([])

  useEffect(() => {
    fetch("/logs")
      .then(res => res.json())
      .then(setLogs)
      .catch(console.error)
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-2">Logs</h1>
      <ul className="space-y-2">
        {logs.map((log, i) => (
          <li key={i} className="bg-white p-2 rounded shadow">
            {JSON.stringify(log.fields)}
          </li>
        ))}
      </ul>
    </div>
  )
}
