import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from "@/components/ui/table";
import { MotionDiv } from "framer-motion";
import Image from "next/image";

const FantasySportsbook = () => {
  const [betSlip, setBetSlip] = useState([]);
  const [fantasyTeams, setFantasyTeams] = useState([]);

  useEffect(() => {
    // Load the predefined fantasy matchup JSON file
    fetch("/mnt/data/fantasy_matchup_upload.json")
      .then(response => response.json())
      .then(data => {
        const teams = data.map((item, index) => [
          { id: index, name: "The Gridion Grandpas", player: item["Team 1 Player"], odds: item["Team 1 Points"], img: "/mnt/data/4329ABF7-94BF-4073-8CA8-7ED37302BD69.png" },
          { id: index + 100, name: "Graveskowski Marches on", player: item["Team 2 Player"], odds: item["Team 2 Points"], img: "/mnt/data/CF878958-A74B-4CCE-881B-6F66B4005940.webp" }
        ]).flat();
        setFantasyTeams(teams);
      });
  }, []);

  const addToBetSlip = (team) => {
    setBetSlip([...betSlip, team]);
  };

  const calculateOdds = () => {
    return betSlip.reduce((acc, team) => acc * team.odds, 1).toFixed(2);
  };

  return (
    <div className="p-6 bg-cover bg-center" style={{ backgroundImage: 'url(/mnt/data/A_sleek,_modern_sportsbook_background_for_Fantasy_.png)' }}>
      <div className="flex justify-center mb-6">
        <Image src="/mnt/data/IMG_9766-remove-background.com.png" alt="Fantasy Champions Logo" width={300} height={100} />
      </div>
      <h1 className="text-2xl font-bold mb-4 text-white">Fantasy Champions Sportsbook</h1>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Team</TableHead>
            <TableHead>Player</TableHead>
            <TableHead>Odds</TableHead>
            <TableHead>Action</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {fantasyTeams.map((team) => (
            <TableRow key={team.id}>
              <TableCell>
                <div className="flex items-center space-x-2">
                  <Image src={team.img} alt={team.name} width={50} height={50} className="rounded-full" />
                  <span>{team.name}</span>
                </div>
              </TableCell>
              <TableCell>{team.player}</TableCell>
              <TableCell>{team.odds}</TableCell>
              <TableCell>
                <Button onClick={() => addToBetSlip(team)}>Add to BetSlip</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      
      <Card className="mt-6 bg-gray-900 text-white">
        <CardContent>
          <h2 className="text-xl font-semibold">Bet Slip</h2>
          {betSlip.length > 0 ? (
            <ul>
              {betSlip.map((bet, index) => (
                <li key={index}>{bet.name} - {bet.odds}</li>
              ))}
            </ul>
          ) : (
            <p>No bets placed yet.</p>
          )}
          <p className="mt-4 font-semibold">Total Odds: {calculateOdds()}</p>
        </CardContent>
      </Card>
    </div>
  );
};

export default FantasySportsbook;
