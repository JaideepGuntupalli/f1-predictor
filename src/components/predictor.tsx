import Image from "next/image";
import {roundsAvailable, roundsCurrent} from "../data/rounds";
import {drivers} from "../data/drivers";
import React, {useState} from "react";
import {NEXT_PUBLIC_API_URL} from "../lib/constants";

const Predictor = () => {
    const [round, setRound] = useState(0);
    const [driver, setDriver] = useState(0);
    const [quali, setQuali] = useState(0);

    const [prediction, setPrediction] = useState(-1);
    const [loading, setLoading] = useState(false);

    // make a request to the API
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        setLoading(true);
        setPrediction(-2);

        let myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        let circuit = roundsCurrent[round];

        if (round == 1) {
            circuit = roundsAvailable[7];
        } else if (round == 4) {
            circuit = roundsAvailable[7];
        } else if (round == 21) {
            circuit = roundsAvailable[5];
        } else if (round == 17) {
            circuit = roundsAvailable[4];
        } else if (round == 5) {
            circuit = roundsAvailable[27];
        }

        let raw = JSON.stringify({
            name: drivers[driver],
            round: circuit,
            qualifying_pos: quali.toString(),
        });

        console.log("Form submitted!");

        await fetch(`${NEXT_PUBLIC_API_URL}/predictGrid`, {
            method: "POST",
            headers: myHeaders,
            body: raw,
        })
            .then((response) => response.json())
            .then((result) => {
                setPrediction(result[0]);
                setLoading(false);
            })
            .catch((error) => {
                setPrediction(0);
                console.log("error", error);
                setLoading(false);
            });
    };

    return (
        <>
            <div className="flex flex-col justify-center gap-4">
                <Image
                    src={"/f1-dark.png"}
                    width={100}
                    height={100}
                    alt={"Formula One Logo"}
                />
                <h1 className="text-4xl font-semibold m-0">Result Predictor</h1>
                <h2 className="text-xl opacity-60 m-0">Based on the Qualifying Position</h2>
            </div>
            <form
                className="my-10 flex w-full max-w-md flex-col gap-4 rounded-lg border-[1px] border-stone-800 bg-[#E6002B]/30 backdrop-blur-2xl p-8"
                onSubmit={handleSubmit}
            >
                <label className="flex flex-col gap-2 text-sm">
                    Year:
                    <input
                        className="rounded-lg border-[1px] border-stone-700 bg-stone-900 px-2 py-2 text-white outline-white"
                        type="number"
                        disabled
                        value={2023}
                    />
                </label>
                <label className="flex flex-col gap-2 text-sm">
                    Circuit:
                    <select
                        className="rounded-lg border-[1px] border-stone-700 bg-stone-900 px-2 py-2 text-white outline-white"
                        onChange={(e) => setRound(Number(e.target.value))}
                    >
                        {Object.entries(roundsCurrent).map(([key, value]) => (
                            <option key={key} value={key}>
                                {value}
                            </option>
                        ))}
                    </select>
                </label>
                <label className="flex flex-col gap-2 text-sm">
                    Driver:
                    <select
                        className="rounded-lg border-[1px] border-stone-700 bg-stone-900 px-2 py-2 text-white outline-white"
                        onChange={(e) => setDriver(Number(e.target.value))}
                    >
                        {Object.entries(drivers).map(([key, value]) => (
                            <option key={key} value={key}>
                                {value}
                            </option>
                        ))}
                    </select>
                </label>
                <label className="flex flex-col gap-2 text-sm">
                    Qualifying Position:
                    <input
                        className="rounded-lg border-[1px] border-stone-700 bg-stone-900 px-2 py-2 text-white outline-white"
                        type="number"
                        onChange={(e) => setQuali(Number(e.target.value))}
                    />
                </label>
                <button
                    className="rounded-lg bg-white p-2 text-sm font-medium text-black transition-all ease-in-out hover:shadow-2xl disabled:bg-orange-900"
                    type="submit"
                >
                    🪄 Predict
                </button>
            </form>
            {prediction != -1 && (
                <section className="my-10 flex w-full max-w-md flex-col gap-4 rounded-lg border-[1px] border-stone-800 bg-[#111111] p-8">
                    <h2 className="text-xl font-medium m-0">Prediction:</h2>
                    <section className="flex w-full max-w-md flex-col gap-4 rounded-lg border-[1px] border-stone-500 bg-[#161616] p-8">
                        <p className="text-center font-medium text-2xl"> {!loading ? (prediction == 1 ? "🏅Podium Finish!": (prediction == 2 ? "🔢 Points Finish!" : (prediction == 3 ? "🅾️ Out of Points!": "🛑 Something went wrong!!"))) : ("Loading...")} </p>
                    </section>
                </section>)}
        </>
    )
}

export default Predictor;